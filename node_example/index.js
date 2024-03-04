import express from "express";

const app = express();

app.use((req, res, next) => {
  console.log(req.method, req.url);
  next();
});

app.get("/", (req, res) => {
  res.send("<h1>Hello, world!<h1>");
});

app.listen(3000, () => {
  console.log("Server listening on port 3000...");
});
