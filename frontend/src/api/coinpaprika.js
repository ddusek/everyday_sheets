import axios from 'axios';
import APIURL from './apiUrl';

const fetch = () => {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    return axios
        .get(`${APIURL}coinpaprika`)
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
