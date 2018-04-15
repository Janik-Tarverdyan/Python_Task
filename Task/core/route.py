from core import controller, task


class Base:

    @task.route('/')
    def home():
        return controller.Page.Home()

    @task.route('/api/new_rate', methods=['GET', 'POST'])
    def new_rate():
        return controller.Page.New_Rate()



class Errors:

    # Error handlers
    def Handler():
        @task.errorhandler(400)
        def bad_request(Error):
            return controller.Error.NO_400(Error)

        @task.errorhandler(401)
        def unauthorized_page(Error):
            return controller.Error.NO_401(Error)

        @task.errorhandler(403)
        def forbidden_page(Error):
            return controller.Error.NO_403(Error)

        @task.errorhandler(404)
        def page_not_found(Error):
            return controller.Error.NO_404(Error)

        @task.errorhandler(405)
        def method_not_allowed(Error):
            return controller.Error.NO_405(Error)

        @task.errorhandler(500)
        def server_Error_page(Error):
            return controller.Error.NO_505(Error)
