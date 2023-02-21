from flask import render_template
from CTFd.utils.decorators import authed_only
from CTFd.utils.user import get_current_user
from CTFd.utils.user import (
    get_current_user,
    get_current_user_attrs
)

def load(app):
    @app.route('/vpn', methods=['GET'])
    @authed_only
    def view_faq():
        user = get_current_user()
        return render_template('page.html', content="<h1>vpn Test</h1><br><p>"+str(user)+"</p>")
