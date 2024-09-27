from flask import Blueprint, request, render_template
from app.utils.search_utils import perform_search

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET', 'POST'])
def search_logs():
    if request.method == 'POST':
        query = request.form.get('query', '')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        limit = int(request.form.get('limit', 100))
    else:
        query = request.args.get('query', '')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        limit = int(request.args.get('limit', 100))
    
    # results = perform_search(query, start_date, end_date, limit)
    
    return render_template('search_results.html', results=[])
