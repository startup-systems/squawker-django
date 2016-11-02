# add this near the top
import dj_database_url

# replace the DATABASES config
DATABASES = {
    "default": dj_database_url.config(default='sqlite:///db.sqlite3'),
}
