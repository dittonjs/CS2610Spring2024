import { useEffect } from "react"
import { Link } from "react-router-dom"
import { useApi } from "../../utils/api"
import { useGroceryLists } from "../../utils/use_grocery_lists"

export const Home = () => {
  const [groceryLists, deleteGroceryList, groceryListsLoading] = useGroceryLists();

  return (
    <div>
      <Link to="/grocery_list/new">Create new list</Link>
      <div>
        {
          groceryLists.map(list => (
            <div key={list.id}>
              <Link to={`/grocery_list/${list.id}`}>{list.name}</Link>
              <button onClick={() => deleteGroceryList(list)}>
              <span className="material-symbols-outlined">delete</span>
              </button>
            </div>
          ))
        }
      </div>
    </div>
  )
}