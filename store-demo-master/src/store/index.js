import { defineStore } from 'pinia'

const UserList0 = defineStore('UserList', {
   state: () => ({
      users: [
         {
            name: 'Alex'
         },
         {
            name: 'Vasya'
         }
      ]
   }),

   getters: {
      Users: (state) => state.users,
   },

   actions: {
      Append(n)
      {
         this.users.push({
            name: n,
         })
      }
   }
})

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

const UserList = defineStore('UserList', {
   state: () => ({
      users: [
         {
            user_id: 1,
            name: 'username',
            surname: 'usersurname',
            school_class: 10,
            subjects: ['m', 'p'],
            messages_places: ['Telegram', 'Mail']
         }
      ]
   }),
   getters: {
      Users: (state) => state.users,
   }
})


export { UserList }
export { OlimpList }