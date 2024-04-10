import { useEffect, useState } from "react";
import { useApi } from "./api";

export const useGroceryList = (id) => {
  const api = useApi();
  const [groceryList, setGroceryList] = useState(null);
  const [loading, setLoading] = useState(true);

  async function loadGroceryList() {
    const {groceryList} = await api.get(`/grocery_lists/${id}/`);
    setGroceryList(groceryList);
    setLoading(false);
  }

  async function purchaseItem(item) {
    const index = groceryList.items.indexOf(item);
    const itemCopy = {...groceryList.items[index]};
    itemCopy.purchased = !itemCopy.purchased;
    const groceryListCopy = {
      ...groceryList,
      items: [...groceryList.items]
    };
    groceryListCopy.items[index] = itemCopy;
    setGroceryList(groceryListCopy);

    const {success} = await api.put(`/grocery_lists/${id}/items/${item.id}/`)
    if (!success) {
      // undo that
      setGroceryList(groceryList); // old state

      // TODO show the user something state that says something went wrong
    }
  }

  useEffect(() => {
    loadGroceryList();
  }, []);

  return [groceryList, purchaseItem, loading];
}