import React, { Component } from 'react'
import { Table } from '@uyun/components'
import { Link } from 'react-router-dom'
import axios from 'axios'

const { Column } = Table

export default class ShowTodo extends Component {
  state = {
    agents: []
  }

  componentDidMount () {
    axios.get('/processmanger/frontapi/v1/queryOS/').then(res => {
      const result = res.data
      this.state.agents = result.message
      this.setState({ agents: this.state.agents })
    })
  }

  render () {
    return (
      <Table dataSource={this.state.agents}>
        <Column
          title="序号"
          dataIndex="key"
          key="key"
        />
        <Column
          title="机器名称"
          dataIndex="name"
          key="name"
        />
        <Column
          title="IP地址"
          dataIndex="ip"
          key="ip"
        />
        <Column
          title="运行状态"
          dataIndex="status"
          key="status"
        />
        <Column
          title="操作"
          key="action"
          render={(row) => {
            if (row.status === '在线') {
              return (<span><Link to={{ pathname: `/process/agent/${row.id}/` }}>查看系统进程</Link></span>)
            } else { return (<span> </span>) }
          }
          }
        />
      </Table>
    )
  }
}
