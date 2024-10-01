from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from app.utils.db import db
from app.utils.db import AuditLog

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = db.users.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            AuditLog(f"User '{username}' logged in successfully").save()
            return redirect(url_for('main.index'))
        else:
            AuditLog(f"Failed login attempt for user '{username}'", level="WARNING").save()
            flash('Invalid username or password')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    user_id = session.get('user_id')
    if user_id:
        user = db.users.find_one({'_id': user_id})
        if user:
            AuditLog(f"User '{user['username']}' logged out").save()
    
    session.clear()
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        
        if db.users.find_one({'username': username}):
            flash('Username already exists')
        else:
            # Create new user
            new_user = {
                'username': username,
                'email': email,
                'password': generate_password_hash(password),
                'role': role
            }
            db.users.insert_one(new_user)
            AuditLog(f"New user '{username}' registered").save()
            flash('Registration successful. Please log in.')
            return redirect(url_for('auth.login'))
    
    return render_template('register.html')

