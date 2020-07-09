import React, { Component } from 'react'
import { Table, Button, Popconfirm } from '@uyun/components'
import axios from 'axios'
import { withRouter } from 'react-router-dom'

const { Column } = Table

@withRouter
export default class KillTodo extends Component {
  state = {
    processInfo: [],
    agentId: ''
  }

  componentDidMount () {
    // 获取agentId
    const agentId = this.props.match.params.agent_id

    // 调用后端接口获取进程
    axios.get(`/processmanger/frontapi/v1/${agentId}/`).then(res => {
      const result = res.data
      this.state.processInfo = result.message
      this.state.agentId = agentId
      this.setState({
        processInfo: this.state.processInfo,
        agentId: this.state.agentId
      })
    })
  }

  killProcess = (agentId, pid, processInfo) => {
    axios.get(`/processmanger/frontapi/v1/${agentId}/${pid}/`).then(res => {
      const data = processInfo.filter(item => parseInt(item.pid) != parseInt(pid))
      this.state.processInfo = data
      this.setState({
        processInfo: this.state.processInfo
      })
    })
  }

  render () {
    const processInfo = this.state.processInfo
    return (
      <div>
        <Table dataSource={processInfo}>
          <Column
            title="PID"
            dataIndex="pid"
            key="pid"
          />
          <Column
            title="进程名称"
            dataIndex="name"
            key="name"
          />
          <Column
            title="命令&参数"
            dataIndex="cmd"
            key="cmd"
            width="15%"
          />
          <Column
            title="CPU使用率"
            dataIndex="cpu_percent"
            key="cpu_percent"
          />
          <Column
            title="内存使用率"
            dataIndex="mem_percent"
            key="mem_percent"
          />
          <Column
            title="虚拟内存占用量"
            dataIndex="virtual_memory"
            key="virtual_memory"
          />
          <Column
            title="创建时间"
            dataIndex="create_time"
            key="create_time"
          />
          <Column
            title="消耗CPU时间"
            dataIndex="cpu_times"
            key="cpu_times"
          />
          <Column
            title="操作"
            key="action"
            render={(text, row, index) => (
              <Popconfirm placement="bottom" title="确定要Kill进程吗？" onConfirm={() => this.killProcess(this.state.agentId, row.pid, this.state.processInfo)} okText="是" cancelText="否">
                <Button type="primary">Kill进程</Button>
              </Popconfirm>
            )}
          />
        </Table>
      </div>
    )
  }
}
