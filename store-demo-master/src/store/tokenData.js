import Vuex from 'vuex';

const userToken = new Vuex.Store({
    state: {
      access_token: '',
      request: "{}",
      reload_page: "/"
    },
    mutations: {
      set_token(state, user_token) {
        state.access_token = user_token;
      },
      set_request(state, new_request) {
        state.request = new_request;
      },
      set_reload_page(state, new_page){
        state.reload_page = new_page;
      }
    },
    getters: {
        get_token: state => {
            return state.access_token;
        },
        get_request: state => {
            return state.request;
        },
        get_reload_page: state => {
            return state.reload_page;
        }
    }
  });

  export { userToken }