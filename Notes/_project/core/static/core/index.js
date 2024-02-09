async function onCheckboxChange(e) {
  // task-id -> taskId
  // taskId -> taskid
  console.log(e.target.dataset.taskId)

  const body = {
    is_completed: e.target.checked,
    objs: [{
      prop1: "asdfasdf"
    }]
  }

  const res = await fetch(`/tasks/${e.target.dataset.taskId}/`, {
    method: "post",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(body)
  });

  console.log(res);
  // do some work

}