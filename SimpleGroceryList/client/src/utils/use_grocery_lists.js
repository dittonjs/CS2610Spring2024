import { useEffect, useState } from "react";
import { useApi } from "./api";

export const useGroceryLists = () => {
  const api = useApi();
  const [groceryLists, setGroceryLists] = useState([]);
  const [loading, setLoading] = useState(true);

  async function loadGroceryLists() {
    const {groceryLists} = await api.get("/grocery_lists/");
    setGroceryLists(groceryLists);
    setLoading(false);
  }

  async function deleteGroceryList(list) {
    setGroceryLists(groceryLists.filter(l => l !== list));
    await api.del(`/grocery_lists/${list.id}/`);
    // undo if failed
  }

  useEffect(() => {
    loadGroceryLists();
  }, []);

  return [groceryLists, deleteGroceryList, loading];
}