import Vue from 'vue';
import App from './components/App.vue';
import store from './store';
import './styles/main.scss';

new Vue({
    el: '#app',
    store,
    render: (h) => h(App),
});
