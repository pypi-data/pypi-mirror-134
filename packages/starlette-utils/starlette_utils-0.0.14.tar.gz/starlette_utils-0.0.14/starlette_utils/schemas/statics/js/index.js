const app = {
    data() {
        return {
            configure_list: []
        }
    },
    created() {
        this.init_data()
    },
    methods: {
        init_data() {
            $.ajax({
                type: 'GET',
                url: "/api/configure/getConfigureList",
                success: (data, textStatus, jqXHR) => {
                    console.log(data)
                    if (data.isSuccess) {
                        this.configure_list = data.data
                    } else {
                        alert(data.message)
                    }
                },
                error: (data, textStatus, jqXHR) => {
                    console.log(data, textStatus, jqXHR)
                }
            });
        }
    }
}