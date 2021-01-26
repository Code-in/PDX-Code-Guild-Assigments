
let app = new Vue({
    el: '#app',
    data: {
        cat_url: '',
        cat_url_array: [],
        cat_array_current_index: 0,
    },
    methods: {
        loadCatPhoto: function() {
            axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/images/search',
            }).then(response => {
                this.cat_url = response.data[0].url
                this.cat_url_array.push(this.cat_url)
                this.cat_array_current_index = this.cat_url_array.length - 1
                console.log(response.data[0].url)
            })
        }, 
        getCatPhoto: function() {
            this.loadCatPhoto()
        },
        seePreviousCatPhoto : function() {
            console.log("seePreviousCatPhoto: "+ this.cat_array_current_index)
            console.log("urls: "+ this.cat_url_array)
            console.log("url to go back to: "+ this.cat_url_array[this.cat_array_current_index])
            if(this.cat_array_current_index > 0) {
                this.cat_array_current_index -= 1
                this.cat_url = this.cat_url_array[this.cat_array_current_index]
            }
        }
    },
    created: function() {
        this.loadCatPhoto()
    }
})
