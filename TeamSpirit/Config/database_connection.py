
def configure_connection(flask_app):
    flask_app.config['MYSQL_HOST'] = 'teamspirit-db.cjjecql31rfh.eu-west-2.rds.amazonaws.com'
    flask_app.config['MYSQL_PORT'] = 3306
    flask_app.config['MYSQL_USER'] = 'root'
    flask_app.config['MYSQL_PASSWORD'] = 'root_password'
    flask_app.config['MYSQL_DB'] = 'teamspiritdb'
    
