import axios from 'axios';

const fetchNews = async () => {
    const APIUrl = 'http://localhost:5000';
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    const fetchReddit = () => {
        axios
            .get(`${APIUrl}/reddit`)
            .then(function (response) {
                return response;
            })
            .catch(function (error) {
                console.log(error);
                return null;
            });
    };
    return fetchReddit();
};

export default {
    fetchNews,
};
