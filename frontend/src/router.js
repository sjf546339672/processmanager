import NotFound from '@/routes/NotFound'
import ShowProcesses from '@/routes/ShowProcesses'
import KillProcess from '@/routes/KillProcess'

export default [
  /**
   * 开发环境跳/login_admin重定向到/
   */
  process.env.NODE_ENV === 'development' && {
    path: '/login_admin',
    redirect: '/'
  },
  {
    path: '/',
    redirect: '/process'
  },
  {
    path: '/process',
    redirect: '/process/show',
    routes: [
      {
        path: '/process/show',
        component: ShowProcesses
      },
      {
        path: '/process/agent/:agent_id',
        component: KillProcess
      }
    ]
  },
  {
    path: '*',
    component: NotFound
  }
].filter(Boolean)
