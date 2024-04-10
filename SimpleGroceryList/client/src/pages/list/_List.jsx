import { useParams } from "react-router"
import { useGroceryList } from "../../utils/use_grocery_list";

export const List = () => {
  const {id} = useParams();
  const [groceryList, purchaseItem, loading] = useGroceryList(id);
  if (loading) {
    return null;
  }
  console.log(groceryList);

  return (
    <div>
      <h2>{groceryList.name}</h2>
      <div>
        {groceryList.items.map(item => (
          <div key={item.id}>
            <input
              type="checkbox"
              checked={item.purchased}
              onChange={() => purchaseItem(item)}
            /> {item.name}
          </div>
        ))}
      </div>
    </div>
  )
}