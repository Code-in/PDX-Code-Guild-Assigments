let app = new Vue({
    el: '#app',
    data: {
        base_url: "http://127.0.0.1:8000",
    },
    methods: {
        loadRequester: function() {
            alert("Hello")
            console.log("Hello")
        }, 
    },
    created: function() {
        this.loadRequester()
    }
})