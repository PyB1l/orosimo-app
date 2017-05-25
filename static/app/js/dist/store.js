'use strict';

function TodoStore() {
  riot.observable(this);

  var store = this;

  store.todos = [{ title: 'Task 1', done: false }, { title: 'Task 2', done: false }];

  store.on('todo_add', function (newTodo) {
    store.todos.push(newTodo);
    store.trigger('todos_changed', store.todos);
  });

  store.on('todo_change', function (todo) {
    store.todos.forEach(function (el) {
      if (el.title === todo.title) {
        el.done = todo.done;
      }
    });
    store.trigger('todos_changed', store.todos);
  });

  store.on('todo_remove', function () {
    store.todos.pop();
    store.trigger('todos_changed', store.todos);
  });

  store.on('todo_init', function () {
    store.trigger('todos_changed', store.todos);
  });
}