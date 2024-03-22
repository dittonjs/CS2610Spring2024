import { useState } from 'react'
let ID_COUNTER = 0;
// content: string
// isCompleted: boolean
// id

function App() {
  const [content, setContent] = useState("");
  const [todos, setTodos] = useState([]);
  console.log(todos);

  function saveTodo(e) {
    e.preventDefault();

    setTodos([
      ...todos,
      {
        content,
        isCompleted: false,
        id: ++ID_COUNTER
      }
    ]);
  }

  function toggleTodo(todo) {

    const index = todos.indexOf(todo);
    // const index = todos.findIndex(other => other.id === todo.id);
    const newTodos = [...todos];
    newTodos[index] = {
      ...todo,
      isCompleted: !todo.isCompleted,
      content: todo.content + " I was modified"
    };
    setTodos(newTodos);
  }

  return (
    <>
      <form onSubmit={saveTodo}>
        <div>Input your todo item</div>
        <input type="text" value={content} onChange={e => setContent(e.target.value)} />
        <button>Save</button>
      </form>
      <div>
        {
          todos.map(todo => (
            <div key={todo.id}>
              <input type="checkbox" checked={todo.isCompleted} onChange={() => toggleTodo(todo)}/> {todo.content}
            </div>
          ))
        }
      </div>
    </>
  )
}

export default App
