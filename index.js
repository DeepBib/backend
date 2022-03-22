const express = require('express');
const axios = require('axios');
const xml2js = require('xml2js');
const { response } = require('express');
const app = express();
const PORT = process.env.PORT || 3000;
const SPRINGER_API_KEY = process.env.SPRINGER_API_KEY;
const NODE_ENV = process.env.NODE_ENV;

if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config();
}

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
            console.log(typeof(result.feed.entry));
            res.status(200).json(result.feed.entry);
        });
    })
    .catch(error => {
        res.send(error);
        console.log(error);
    });
});

app.get('/springer/:keyword', (req, res) => {
    const keyword = req.params.keyword;
    console.log("hi ", keyword);
    axios.get(`http://api.springernature.com/metadata/json?q=keyword:${keyword}&api_key=${SPRINGER_API_KEY}`)
    .then(response => {
        console.log(typeof(response.data));
        // console.log(response);
        res.status(200).json(response.data.records);
    }).catch(error => {
        res.send(error);
        console.log(error);
    });
})

app.get('/ieee', (req, res) => res.send('Salut IEEE!'));

app.listen(PORT, () => {
    console.log(`Example app listening on port ${PORT}!`)
});