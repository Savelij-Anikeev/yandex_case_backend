#API.
#Add 

headers: `Authorization: Token 'token'`.

1) authorization:

        auth/users/  - (METHODS: GET/POST) create or get list of users (authorized only)
        auth/users/me/ - (METHODS: GET) current user (authorized only)
        auth/token/login/ - (METHODS: POST) send `username` and `password` to login and get token
        auth/token/logout/ - (METHODS: GET) empty requiest to logout

3) api:

        api/v1/groups/ - (METHODS: GET) получить список всех групп (они выступают как роли)
        api/v1/groups/user/<user_id>/ - (METHODS: GET, PATH, PUT) установить группу у пользователя с id = <user_id>
                                        передав `group` (список с индексами групп)
        api/v1/events/ - (METHODS: GET, POST) получить ваще все мероприятия базарю
        api/v1/events/<id>/ - (METHODS: GET, POST, PATCH, PUT, DELETE) круд с ивентом id = <id>. Но только если ты админ или автор ивента
        api/v1/user-event-rel/ - (METHODS: GET, POST) - (GET) вывести все отношения между пользователем и
                                                        (POST) ивентом  или создать отношения  (когда он записывается на меро)
        api/v1/user-event-rel/<id>/ - (METHODS: GET, POST) - знать айди отношения не нужно, просто обратиться по айди ивента,
                                                             юзера определять не надо, он подхватывается автоматически. Если админ, то
                                                             выводятся все записи, если пользователь, то только его
        api/v1/categories/ - (METHODS: GET) получить все категории, добавлять может только админимтсратор
        api/v1/categories/<id>/ - (METHODS: GET) получить категорию по id
        //// eto govnocod kostyl, potom perepishu, bez etogo rabotaet
        ////api/v1/event-category-rel/ - (METHODS: GET, POST) - create or get all relations
        ////api/v1/event-category-rel/<id>/ - (METHODS: GET, POST) -
        ////
         



       
