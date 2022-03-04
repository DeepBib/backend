const express = require('express');
const axios = require('axios');
const xml2js = require('xml2js');
const app = express();
const port = 8080;

app.get('/', (req, res) => res.send('Hello World!'));

app.get('/articles/:query', (req,res) => {
    const query = req.params.query;
    axios.get(`http://export.arxiv.org/api/query?search_query=all:${query}&max_results=10`)
    .then(response => {
        const xmlRes = response.data;
        xml2js.parseString(xmlRes, (err, result) => {
            if(err) {
                console.log(error);
            }
            res.status(200).json(result.feed.entry);
        });
    })
    .catch(error => {
        console.log(error);
    });
})


app.listen(port, () => {
    console.log(`Example app listening on port ${port}!`)
});