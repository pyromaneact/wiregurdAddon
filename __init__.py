from flask import render_template
from wireguard_tools import WireguardKey
from CTFd.models import Users, db
from CTFd.utils.decorators import authed_only
from CTFd.utils.user import (
    get_current_user,
    get_current_user_attrs
)

#add table for storing each users vpn connection
class VPNConnection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    privateKey = db.Column(db.String(50))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))


#generate and return private key for VPN
def keyGen():
    private_key = WireguardKey.generate()
    public_key = private_key.public_key()
    return str(private_key)


def load(app):
    app.db.create_all()
    @app.route('/vpn', methods=['GET'])

    #only allow authed users to acces page ( I'm sure there is a reson CTFD uses this then checks agin later but I dont care and aint going to fix it
    @authed_only

    def view_faq():
        #extract vpn details
        userid = get_current_user().id
        details = VPNConnection.query.filter_by(id=userid).first()

        #if vpn details dont exsist create them ( make a function later lazy man)

#	this code dose not exicute the update or at least dosnt seem too gather the data after running unable to get details to not = nonetype
#	hours wasted: 3 and counting

        if type(details) == None.__class__:
            private =  keyGen()
            db.session.add(VPNConnection(privateKey = private, user = userid))
            db.session.commit()
            details = VPNConnection.query.filter_by(id=userid).first()
            return render_template('page.html', content="<h1>vpn Test added details:</h1><br><p>"+ str(details.privateKey)+"</p>")

        else:

            return render_template('page.html', content="<h1>vpn Test</h1><br>"+ str(details.privateKey)+"<br><p></p>")
