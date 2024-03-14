
import axios from 'axios'

const api_backend = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1/",
  });

  
export const ENDPOINTS ={
setAuthorization:(token)=>{
    api_backend.defaults.headers.Authorization = `Bearer ${token}`;
},

getAuthorization:()=>{
    api_backend.defaults.headers.Authorization?.replace('Bearer ', '');
},

removeAuthorization:()=>{
    api_backend.defaults.headers.Authorization;
},

register: async (formData)=>{
    try{
        const res = await api_backend.post('account/register', formData)
        return res
    }catch(err){
        console.log(err)
    }
},

login: (formData)=>{
    try{
        const res = api_backend.post('account/login', formData)
        return res
    }catch(err){
        console.log(err)
    }
},

getTask:(trader_id)=>{
    const res = api_backend.get(`tasks/${trader_id}`)
    return res.data
}
,
getAllTasks: ()=>{
    const res = api_backend.get('tasks')
    return res
},

fetchAnalytics: ()=>{
    const res = api_backend.get('analytics')
    return res
},

updateTask:(task_id)=>{
    const res = api_backend.patch(`tasks/${task_id}`)
    return res
}
}

export default ENDPOINTS