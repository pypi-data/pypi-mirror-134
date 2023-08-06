const app = {
    data() {
        return {
            is_login: false,
            username: ''
        }
    },
    created() {
        this.check_login()
    },
    methods: {
        check_login() {
            var cookie_access = getCookie('access')
            if (cookie_access) {
                this.is_login = true
                $.ajax({
                    type: 'GET',
                    url: "/api/configure/getConfigureList",
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("Authorization", 'access ' + cookie_access);
                    },
                    success: (data, textStatus, jqXHR) => {
                        if (data.isSuccess) {
                            this.username = data.content.username
                        } else {
                            alert(data.errorMessage)
                        }
                    },
                    error: (data, textStatus, jqXHR) => {
                        console.log(data, textStatus, jqXHR)
                    }
                });
            } else {
                this.is_login = false
                this.username = ''
            }
        },
        logout() {
            delCookie('access')
            this.check_login()
        }
    }
}