<script setup>
import router from '@/router';
import { userToken } from '@/store/tokenData';


router.push(userToken.getters.get_reload_page);
</script>