class Blog:

    route_app_labels = {"blog"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "db_blog"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "db_blog"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "db_blog"
        return None


class Kontak:

    route_app_labels = {"kontak"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "db_kontak"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "db_kontak"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "db_kontak"
        return None
