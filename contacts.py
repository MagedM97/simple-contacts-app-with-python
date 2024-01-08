import flask

app =flask.Flask("contacts")
app = flask.Flask(__name__,static_url_path='/static')

def html(page):
    html_page = open(page + ".html")
    html_content = html_page.read()
    html_page.close()
    return html_content

def getcontacts():
    contacts = open("contacts.txt")
    content = contacts.read()
    contacts.close()
    my_contacts= content.split("\n")
    return my_contacts

@app.route("/")
def homepage():
    return html("index")

@app.route("/contacts")
def contactspage():
    my_contacts = getcontacts()
    contactspage=html("contacts")
    contacts_list = ""
    search = flask.request.args.get("search")
    if search:
        for contact in my_contacts:
            if search.lower() in contact.lower() :
                contacts_list += "<li>" + contact + "</li>"
        if contacts_list != "":
            return contactspage.replace("$contacts$", contacts_list)
        else:
            return contactspage.replace("$contacts$", "No similar contacts")
    else:
        for contact in my_contacts:
            contacts_list += "<li>" + contact + "</li>"
    
        return contactspage.replace("$contacts$", contacts_list)