export function WelcomeMessage({ user }) {
  return (
    <div>
      <p>Welcome to my application, {user.name}!</p>
      {
        user.isAdmin ? (
          <div>You are the admin!</div>
        ) : (
          null
        )
      }
    </div>
  )
}

