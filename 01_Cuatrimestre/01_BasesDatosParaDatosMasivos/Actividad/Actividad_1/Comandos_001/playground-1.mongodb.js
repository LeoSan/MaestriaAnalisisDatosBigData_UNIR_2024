/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

/*const database = 'miscelanea';
const collection = 'books';
const collection2 = 'companies';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection(collection);
db.createCollection(collection2); */

db.getCollection('books').find({longDescription: {$gte: "A", $lt: "B"}}, {title: 1, longDescription: 1})


