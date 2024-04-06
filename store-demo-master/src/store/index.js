import { defineStore } from 'pinia'

const OlimpList = defineStore('OlimpList', {
   state: () => ({
      olimps: [
         {
            olimp_id: 1,
            name: 'olimp1',
            description: 'desc1',
            olimp_classes: [1, 2, 3],
            subjects: ['m', 'p'],
            href_to_olimp: 'https1',
         },
         {
            olimp_id: 2,
            name: 'olimp2',
            description: 'desc2',
            olimp_classes: [2, 3, 4],
            subjects: ['e', 's'],
            href_to_olimp: 'https2',
         }
      ]
   }),
   getters: {
      Olimps: (state) => state.olimps,
   }

})




export { OlimpList }