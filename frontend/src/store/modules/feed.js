import news from '../../api/news';

const state = () => ({
    items: [],
});

const getters = {
    redditFeeds: (state) => {
        return state.items.map((i) => {
            return {
                header: i.title,
                url1: i.link_url,
                url2: i.reddit_url,
                additionalInfo: i.rating,
            };
        });
    },
};

const actions = {
    async getNewsAsync({ commit }) {
        const data = news.fetchNews();
        commit('setNewsState', await data);
    },
};

const mutations = {
    setNewsState(state, data) {
        state.items = data;
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};
