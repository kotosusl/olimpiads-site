import { defineStore } from 'pinia'

const OlimpList = defineStore('OlimpList', {
   state: () => ({
      olimps: [
         {
            'id': 1,
            'name': 'Бельчонок gafdhsf dafsgmdh sFDgzfxc',
            'href': '/1234',
            'desc': 'самая лучшая олимпиада, омг',
            'min_class': 1,
            'max_class': 11,
            'subjects': ['информатика', 'math', 'weqfqr', 'rbqerbq', 'wrqrrthn', 'wyynbgrvf']
        },
        {
         'id': 2,
         'name': 'Бельчонок',
         'href': '/1234',
         'desc': 'самая лучшая олимпиада, омг',
         'min_class': 1,
         'max_class': 11,
         'subjects': ['информатика', 'math', 'weqfqr', 'rbqerbq']
     },
     {
      'id': 3,
      'name': 'Бельчонок',
      'href': '/1234',
      'desc': 'самая лучшая олимпиада, омг',
      'min_class': 1,
      'max_class': 11,
      'subjects': ['информатика', 'math', 'weqfqr', 'rbqerbq']
  },
  {
   'id': 4,
   'name': 'Бельчонок',
   'href': '/1234',
   'desc': 'самая лучшая олимпиада, омг',
   'min_class': 1,
   'max_class': 11,
   'subjects': ['информатика', 'math', 'weqfqr', 'rbqerbq']
},
{
   'id': 5,
   'name': 'Бельчонок',
   'href': '/1234',
   'desc': 'самая лучшая олимпиада, омг',
   'min_class': 1,
   'max_class': 11,
   'subjects': ['информатика', 'math', 'weqfqr', 'rbqerbq', 'wrqrrthn', 'wyynbgrvf']
},
      ]
   }),
   getters: {
      Olimps: (state) => state.olimps,
   }

})




export { OlimpList }