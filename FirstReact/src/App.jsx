
function App() {
  return (
    <div>
      <h1>Hello, world!</h1>
      <WelcomeMessage name="Catelyn" isAdmin={true}/>
    </div>
  );
}

function WelcomeMessage(props) {
  return (
    <div>
      <p>Welcome to my application, {props.name}!</p>
      {
        props.isAdmin ? (
          <div>You are the admin!</div>
        ) : (
          null
        )
      }
    </div>
  )
}

export default App
