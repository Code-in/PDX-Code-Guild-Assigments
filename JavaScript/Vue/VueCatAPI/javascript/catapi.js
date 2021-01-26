
let app = new Vue({
    el: '#app',
    data: {
        cat_url: '',
        cat_url_array: [],
        cat_array_current_index: 0,
        selected_cat_category: '',
        cat_catagories: [{"id":0,"name":"Any"}],
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
            if(this.selected_cat_category.name === 'Any') {
                this.loadCatPhoto()
            } else {
                this.getCatPhotoFromCatagory()
            }
        },
        seePreviousCatPhoto : function() {
            console.log("seePreviousCatPhoto: "+ this.cat_array_current_index)
            console.log("urls: "+ this.cat_url_array)
            console.log("url to go back to: "+ this.cat_url_array[this.cat_array_current_index])
            if(this.cat_array_current_index > 0) {
                this.cat_array_current_index -= 1
                this.cat_url = this.cat_url_array[this.cat_array_current_index]
            }
        },
        getCatagoryList: function() {
            axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/categories',
            }).then(response => {
                this.cat_catagories.push.apply(this.cat_catagories, response.data)
                this.selected_cat_category = this.cat_catagories[0]
                console.log(this.cat_catagories)
            })
        },
         getCatPhotoFromCatagory: function() {
            axios({
                method: 'get',
                url: 'https://api.thecatapi.com/v1/images/search?category_ids=' + this.selected_cat_category.id,
            }).then(response => {
                this.cat_url = response.data[0].url
                this.cat_url_array.push(this.cat_url)
                this.cat_array_current_index = this.cat_url_array.length - 1
                console.log(response.data)
            })
        }
    },
    filters: {
        capitalize: function (value) {
            if (!value) return ''
            value = value.toString()
            return value.charAt(0).toUpperCase() + value.slice(1)
        }
    },
    created: function() {
        this.loadCatPhoto()
        this.getCatagoryList()
    }
})


