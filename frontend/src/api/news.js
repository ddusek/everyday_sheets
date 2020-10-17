import axios from 'axios';

const fetchNews = () => {
    const APIUrl = 'http://localhost:5000';
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    const fetchReddit = () => {
        return axios
            .get(`${APIUrl}/reddit`)
            .then((response) => {
                return response.data;
            })
            .catch((error) => {
                console.log(error);
                return null;
            });
    };
    return fetchReddit();
};

export default {
    fetchNews,
};
