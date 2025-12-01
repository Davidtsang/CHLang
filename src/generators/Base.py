class CodeGenerator:
    def generate(self, context):
        raise NotImplementedError

    # 辅助函数：标准化方法信息
    def get_method_info(self, m_name, m_info):
        res = {}
        if hasattr(m_info, 'name'):  # ClassInfo Object
            res['name'] = m_info.name
            res['access'] = m_info.access
            res['args'] = [{'type': a.type} for a in m_info.args]
        else:  # Dict
            res['name'] = m_info.get('name')
            res['access'] = m_info.get('access', 'private')
            res['args'] = m_info.get('args', [])
        return res