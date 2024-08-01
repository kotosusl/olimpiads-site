import { defineStore } from 'pinia'

const OlimpList = defineStore('OlimpList', {
    state: () => ({
       'success': 'OK',
                'olimp': {
                    'id': 1,
                    'name': 'Бельчонок',
                    'href': '/1234',
                    'desc': 'самая лучшая олимпиада, омг',
                    'min_class': 1,
                    'max_class': 11,
                    'subjects': ['информатика', 'math', 'weqfqr', 'rbqerbq']
                }
    }),
    getters: {
       Users: (state) => state.users,
    }
 })

 export { OlimpList }