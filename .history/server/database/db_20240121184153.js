import dotenv from 'dotenv';
dotenv.config();

import { MongoClient, ServerApiVersion } from 'mongodb';

// Use environment variables for the credentials
//const uri = `mongodb+srv://${process.env.DB_USERNAME}:${process.env.DB_PASSWORD}@2920.6waixsq.mongodb.net/?retryWrites=true&w=majority`;
const uri = 'mongodb+svr://127.0.0.1:53677/cbefe1f4-ace8-48dd-ab02-baab9012145c?';

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
    serverApi: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
});

async function run() {
    try {
        // Connect the client to the server (optional starting in v4.7)
        await client.connect();
        // Send a ping to confirm a successful connection
        await client.db("admin").command({ ping: 1 });
        console.log("Pinged your deployment. You successfully connected to MongoDB!");
    } finally {
        // Ensures that the client will close when you finish/error
        await client.close();
    }
}
export { client, run };

