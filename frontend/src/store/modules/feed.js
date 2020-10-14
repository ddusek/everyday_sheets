import news from '../../api/news';

const state = () => ({
    items: [],
});

const getters = {
    feeds: (state) => {
        return state.items.map((i) => {
            return {
                header: i.title,
                additionalInfo: i.rating,
                url1: i.link_url,
                ur2: i.link_url,
            };
        });
    },
};

const actions = {
    getNews({ commit }) {
        commit('getNewsFromApi');
    },
};

const mutations = {
    getNewsFromApi(state) {
        state.feeds = news.fetchNews();
    },
};
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};
