

let input_todo = document.querySelector('#input_todo')
let input_notes = document.querySelector('#input_notes')
let input_date = document.querySelector('#input_date')
let btn_add = document.querySelector('#btn_add')
let table_todo = document.querySelector('#table_todo')
let table_done = document.querySelector('#table_done')
let div_alert = document.querySelector('#div_alert')
let input_search = document.querySelector('#searchField')

window.onload = (event) => {
    console.log('page is fully loaded');
    //saveData('todoList', null) // Clean out DOM Data when needed
    //saveData('doneList', null) // Clean out DOM Data when needed
    let todoList = readData('todoList')
    console.log("todoList Data:" + todoList)
    if (todoList != null) {
        console.log("Update DOM drawning with data")
        console.log(todoList)
        console.log("Dom len: " + todoList.length)
        for (x = 0; x < todoList.length; x++) {
            // Draw DOM
            console.log('uuid:' + todoList[x]['uuid'] + 'todo: ' + todoList[x]['todo'] + 'notes: ' + todoList[x]['notes'] + 'date: ' + todoList[x]['date'])
            drawTodoItems(todoList[x]['uuid'], todoList[x]['todo'], todoList[x]['notes'], todoList[x]['date'])
        }
    } else {
        console.log("No data to update DOM")
    }
    let doneList = readData('doneList')
    console.log("doneList Data:" + doneList)
    if (doneList != null) {
        console.log("Update doneList drawning with data")
        console.log(doneList)
        console.log("doneList len: " + doneList.length)
        console.table(doneList)
        for (x = 0; x < doneList.length; x++) {
            // Draw DOM
            console.log('uuid:' + doneList[x]['uuid'] + 'todo: ' + doneList[x]['todo'] + 'notes: ' + doneList[x]['notes'] + 'date: ' + doneList[x]['date'])
            DrawDoneItems(doneList[x]['uuid'], doneList[x]['todo'], doneList[x]['notes'], doneList[x]['date'])
        }
    } else {
        console.log("No data to update DOM")
    }
}


btn_add.addEventListener('click', function (event) {

    let todo = input_todo.value
    let notes = input_notes.value
    let date = input_date.value
    let uuid = uuidv4()

    console.log("DATE: " + date)
    if(date.includes("-")) {
        date = date.split('-')
        date = date[1] + '/' + date[2] + '/' + date[0]
    }

    // Draw DOM
    drawTodoItems(uuid, todo, notes, date)

    input_todo.value = ''
    input_notes.value = ''

    // The saving section for the added user data
    let len = 0
    let todoList = readData('todoList')
    if (todoList === null) {
        todoList = []
    }

    // This push a new item on the todoList with title, notes and date when you press the "Add" button
    todoList.push({ 'uuid': uuid, 'todo': todo, 'notes': notes, 'date': date })
    console.log(todoList)
    saveData('todoList', todoList)
})

function drawTodoItems(in_uuid, in_todo, in_notes, in_date) {
    let todo = in_todo
    let notes = in_notes
    let date = in_date
    let uuid = in_uuid

    if (uuid === '' || todo === '' || notes === '' || date === '') {
        // alert('Please fill out all fields')
        div_alert.style.display = ''
        setTimeout(function () {
            div_alert.style.display = 'none'
        }, 3000)
        return
    }

    // create tr element
    let tr = document.createElement('tr')

    // create the td for the name
    let td_todo = document.createElement('td')
    td_todo.innerText = todo
    tr.appendChild(td_todo)

    // td for the notes
    let td_notes = document.createElement('td')
    td_notes.innerText = notes
    tr.appendChild(td_notes)

    // td for the date
    let td_date = document.createElement('td')
    td_date.innerText = date
    tr.appendChild(td_date)

    // td for the red button
    let td_red_btn = document.createElement('td')
    let span_remove = document.createElement('span')
    span_remove.innerText = '✕'
    span_remove.classList.add('btn', 'btn-danger')



    // The "RED" X box which should red the todo item from the todoList
    span_remove.addEventListener('click', function (event) {
        console.log("drawTodoItems RED printing target" + event.target.innerHTML)
        console.log("drawTodoItems RED printing tr" + tr.innerHTML)
        table_todo.removeChild(tr)
        var todoList = readData('todoList')
        if(todoList != null) {
            // NOTE this needs to be refactored it's not a clean way of doing this.
            console.log('uuid: ' + tr.dataset.uuid)
            console.table(todoList)
            let index = todoList.findIndex(obj => function (obj) {
                console.log('doneList tr.dataset.uuid:' + tr.dataset.uuid)
                console.log('doneList obj.uuid:' + obj.uuid)
                return obj.uuid === tr.dataset.uuid
            })
            console.log('Red todoList index to delete:' + index)
            if (index != -1) {
                todoList.splice(index, 1);
            }
            saveData('todoList', todoList)
            console.table(todoList)
        }
    })
    td_red_btn.appendChild(span_remove)
    tr.appendChild(td_red_btn)

    // td for the done button
    let td_green_btn = document.createElement('td')
    let span_done = document.createElement('span')
    span_done.innerText = '√'
    span_done.classList.add('btn', 'btn-success')


    // The "GREEN" √ Box which should move the item from the "dotoList" to the "doneList".
    span_done.addEventListener('click', function (event) {
        console.log("drawTodoItems Green printing target" + event.target)
        console.log("drawTodoItems Green printing tr" + tr.innerHTML)
        table_todo.removeChild(tr)
        tr.removeChild(td_green_btn)

        //NOTE this needs to be refactored it's not a clean way of doing this.
        var todoList = readData('todoList')
        if(todoList != null) {
            console.log('uuid: ' + tr.dataset.uuid)
            console.table(todoList)
            let index = todoList.findIndex(function (obj) {
                console.log('todoList tr.dataset.uuid:' + tr.dataset.uuid)
                console.log('todoList obj.uuid:' + obj.uuid)
                return obj.uuid === tr.dataset.uuid
            })
            console.log('Green todoList index to delete:' + index)
            if (index != -1) {
                todoList.splice(index, 1);
            }
            saveData('todoList', todoList)
            console.table(todoList)
        }
        // The "RED" X box which should red the done item from the list "doneList"
        span_remove.addEventListener('click', function (event) {
            console.log("This Click fired off table_done red")
            console.log("drawTodoItems Red printing target" + event.target.innerHTML)
            console.log("drawTodoItems Red printing tr" + tr.innerHTML)
            table_done.removeChild(tr)
            var doneList = readData('doneList')
            // NOTE this needs to be refactored it's not a clean way of doing this.
            console.log('uuid: ' + tr.dataset.uuid)

            let index = doneList.findIndex(function (obj) {
                console.log('doneList tr.dataset.uuid:' + tr.dataset.uuid)
                console.log('doneList obj.uuid:' + obj.uuid)
                return obj.uuid === tr.dataset.uuid
            })
            console.log('doneList index to delete:' + index)
            if (index != -1) {
                doneList.splice(index, 1);
            }
            saveData('doneList', doneList)
            console.table(doneList)
        })

        table_done.appendChild(tr)

        
        // NOTE this needs to be refactored it's not a clean way of doing this.
        var doneList = readData('doneList')
        if(doneList === null) {
            doneList = []
        }
        doneList.push({ 'uuid': tr.dataset.uuid, 'todo': tr.children[0].innerText, 'notes': tr.children[1].innerText, 'date': tr.children[2].innerText })
        saveData('doneList', doneList)
        console.log("Content doneList: ")
        console.table(doneList)
    })

    td_green_btn.appendChild(span_done)
    tr.appendChild(td_green_btn)

    tr.dataset.uuid = uuid
    table_todo.appendChild(tr)

}

function DrawDoneItems(in_uuid, in_todo, in_notes, in_date) {
    let uuid = in_uuid
    let todo = in_todo
    let notes = in_notes
    let date = in_date

    // Set the Yellow alert to remind them to fill out the data
    if (uuid === '' || todo === '' || notes === '' || date === '') {
        // alert('Please fill out all fields')
        div_alert.style.display = ''
        setTimeout(function () {
            div_alert.style.display = 'none'
        }, 3000)
        return
    }

    // create tr element
    let tr = document.createElement('tr')

    // create the td for the name
    let td_todo = document.createElement('td')
    td_todo.innerText = todo
    tr.appendChild(td_todo)

    // td for the notes
    let td_notes = document.createElement('td')
    td_notes.innerText = notes
    tr.appendChild(td_notes)

    // td for the date
    let td_date = document.createElement('td')
    td_date.innerText = date
    tr.appendChild(td_date)

    // td for the red button
    let td_red_btn = document.createElement('td')
    let span_remove = document.createElement('span')
    span_remove.innerText = '✕'
    span_remove.classList.add('btn', 'btn-danger')
    // The "RED" X box which should red the done item from the list
    span_remove.addEventListener('click', function (event) {
        console.log("DrawDoneItems Red printing target" + event.target.innerHTML)
        console.log("DrawDoneItems Red printing tr" + tr.innerHTML)
        table_done.removeChild(tr)
        var doneList = readData('doneList')
        if(doneList != null) {
            // NOTE this needs to be refactored it's not a clean way of doing this.
            console.log('uuid: ' + tr.dataset.uuid)
            console.table(doneList)
            let index = doneList.findIndex(function (obj) {
                console.log('doneList tr.dataset.uuid:' + tr.dataset.uuid)
                console.log('doneList obj.uuid:' + obj.uuid)
                return obj.uuid === tr.dataset.uuid
            })
            console.log('doneList index to delete:' + index)
            if (index != -1) {
                doneList.splice(index, 1);
            }

            saveData('doneList', doneList)
            console.table(doneList)
        }

    })
    td_red_btn.appendChild(span_remove)
    tr.appendChild(td_red_btn)

    tr.dataset.uuid = uuid
    table_done.appendChild(tr)
}


function search() {
    var filter = input_search.value.toLowerCase()

    // Check the todo items
    for (let i = 1; i < table_todo.children.length; i++) {
        let tr = table_todo.children[i]
        console.log(tr)
        console.log("Content: " + tr.textContent)
        if (tr.textContent.toLowerCase().includes(filter)) {
            tr.style.display = ""
        } else {
            tr.style.display = "none"
        }
    }

    // Check the done items as well
    for (let i = 1; i < table_done.children.length; i++) {
        let tr = table_done.children[i]
        console.log(tr)
        console.log("Content: " + tr.textContent)
        if (tr.textContent.toLowerCase().includes(filter)) {
            tr.style.display = ""
        } else {
            tr.style.display = "none"
        }
    }
}


// CRUD methods

// This is a temporary Create and Update
function saveData(name, data) {
    console.table(data)
    console.log("saveData Name:" + name + " data: " + JSON.stringify(data))
    localStorage.setItem(name, JSON.stringify(data))
}


function readData(name) {
    let datum = JSON.parse(localStorage.getItem(name))
    console.log("readData: " + JSON.stringify(datum))
    console.table(name)
    return datum
}

// Note this is off StackOverFlow thus I can't and don't claim it as mine
function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}