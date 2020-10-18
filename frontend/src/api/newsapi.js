import axios from 'axios';
import APIURL from './apiUrl';

const fetch = (key) => {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    return axios
        .get(`${APIURL}newsapi/${key}`)
        .then((response) => {
            return response.data;
        })
        .catch((error) => {
            console.log(error);
            return null;
        });
};

export default {
    fetch,
};
