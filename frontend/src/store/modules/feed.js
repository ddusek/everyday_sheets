import redditApi from '../../api/reddit';
import newsApi from '../../api/newsapi';
import coinpaprikaApi from '../../api/coinpaprika';

const state = () => ({
    items: [],
});

const getters = {};

const actions = {
    async getFeeds({ commit }, payload) {
        let data = [];
        switch (payload.category) {
            case 'reddit':
                data = await redditApi.fetch();
                break;
            case 'newsapi':
                data = await newsApi.fetch(payload.key);
                break;
            case 'coinpaprika':
                data = await coinpaprikaApi.fetch();
                break;
        }
        commit('setItems', data);
        return data;
    },
};

const mutations = {
    setItems(state, payload) {
        state.items = payload;
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};
