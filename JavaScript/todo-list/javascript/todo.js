

let input_todo = document.querySelector('#input_todo')
let input_notes = document.querySelector('#input_notes')
let input_date = document.querySelector('#input_date')
let btn_add = document.querySelector('#btn_add')
let table_todo = document.querySelector('#table_todo')
let table_done = document.querySelector('#table_done')
let div_alert = document.querySelector('#div_alert')
let input_search = document.querySelector('#searchField')


btn_add.addEventListener('click', function(event) {
    
    let todo = input_todo.value
    let notes = input_notes.value
    let date = input_date.value

    if (todo === '' || notes === '' || date === '') {
        // alert('Please fill out all fields')
        div_alert.style.display = ''
        setTimeout(function() {
            div_alert.style.display = 'none'
        }, 3000)
        return
    }

    input_todo.value = ''
    input_notes.value = ''

    date = date.split('-')
    date = date[1] + '/' + date[2] + '/' + date[0]

    // create tr element
    let tr = document.createElement('tr')

    // create the td for the name
    let td_todo = document.createElement('td')
    td_todo.innerText = todo
    tr.appendChild(td_todo)

    let td_notes = document.createElement('td')
    td_notes.innerText = notes
    tr.appendChild(td_notes)

    let td_date = document.createElement('td')
    td_date.innerText = date
    tr.appendChild(td_date)

    let td_btn_remove = document.createElement('td')
    let span_remove = document.createElement('span')
    span_remove.innerText = '✕'
    span_remove.classList.add('btn', 'btn-danger')
    span_remove.addEventListener('click', function(event) {
        table_todo.removeChild(tr)
    })
    td_btn_remove.appendChild(span_remove)
    tr.appendChild(td_btn_remove)

    let td_btn_done = document.createElement('td')
    let span_done = document.createElement('span')
    span_done.innerText = '√'
    span_done.classList.add('btn', 'btn-success')
    span_done.addEventListener('click', function(event) {
        table_todo.removeChild(tr)
        tr.removeChild(td_btn_done)
        span_remove.removeEventListener('click', function(event) {
            table_todo.removeChild(tr)
        })
        span_remove.addEventListener('click', function(event) {
            table_done.removeChild(tr)
        })
        table_done.appendChild(tr)
    })
    td_btn_done.appendChild(span_done)
    tr.appendChild(td_btn_done)

    table_todo.appendChild(tr)
})


function search() {
    var filter = input_search.value.toLowerCase()
    for (let i = 0; i < table_todo.children.length; i++) {
        if(i > 0) {
            let tr = table_todo.children[i]
            console.log(tr)
            if (tr.textContent.toLowerCase().includes(filter)) {
                tr.style.display = ""
            } else {
                tr.style.display = "none"
            }
        }
    }
}