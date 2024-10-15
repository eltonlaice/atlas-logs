from flask import Blueprint, request, render_template

search_bp = Blueprint('search', __name__)


@search_bp.route('/search', methods=['GET', 'POST'])
def search_logs():
    if request.method == 'POST':
        query = request.form.get('query', '')
    else:
        query = request.args.get('query', '')

    # results = perform_search(query, start_date, end_date, limit)
    # Create dummy data for results with audit logs
    results = [
        "2023-06-01 10:15:23 [INFO] User 'john_doe' logged in successfully",
        "2023-06-01 11:30:45 [WARNING] Failed login attempt for user 'jane_smith'",
        "2023-06-02 09:05:12 [ERROR] Database connection timeout",
        "2023-06-02 14:20:37 [INFO] File 'report.pdf' uploaded by user 'admin'",
        "2023-06-03 08:45:59 [WARNING] Disk space usage above 80%",
        "2023-06-03 16:10:28 [INFO] User 'jane_smith' changed password",
        "2023-06-04 11:55:42 [ERROR] API request failed: 404 Not Found",
        "2023-06-04 13:40:15 [INFO] Scheduled maintenance started",
        "2023-06-05 10:30:33 [WARNING] Multiple failed login attempts detected from IP 192.168.1.100",
        "2023-06-05 18:05:51 [INFO] System update completed successfully",
        "2023-06-06 09:20:17 [INFO] New user 'alice_wonder' created",
        "2023-06-06 14:45:30 [ERROR] Out of memory error in process ID 1234",
        "2023-06-07 11:10:55 [WARNING] SSL certificate expiring in 7 days",
        "2023-06-07 16:30:22 [INFO] Backup process completed successfully",
        "2023-06-08 08:55:40 [ERROR] Failed to connect to external API",
        "2023-06-08 13:15:09 [INFO] User 'bob_builder' modified permissions for project 'skyline'",
        "2023-06-09 10:40:28 [WARNING] High CPU usage detected on server 'web-01'",
        "2023-06-09 15:25:37 [INFO] Automated security patch applied",
        "2023-06-10 09:50:14 [ERROR] Database query timeout after 30 seconds",
        "2023-06-10 14:05:53 [INFO] User 'carol_tech' initiated system shutdown"
    ]
    return render_template('search_results.html', results=results)
