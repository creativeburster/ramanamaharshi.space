// Cloudflare Pages Function: /api/contact
export async function onRequestPost(context) {
    const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    };

    try {
        const body = await context.request.json();
        const { name, contact, message } = body;

        if (!name || !contact || !message) {
            return new Response(JSON.stringify({ success: false, message: '请填写完整信息' }), {
                status: 400,
                headers: { 'Content-Type': 'application/json', ...corsHeaders }
            });
        }

        // 目标接收邮箱（仅存在于边缘后端，前端绝不暴露）
        const targetEmail = '591611431@qq.com';

        const forwardPayload = {
            _subject: `【拉玛那知识库】来自读者 ${name} 的留言`,
            _template: 'table',
            _captcha: 'false',
            '读者称呼': name,
            '联系方式': contact,
            '留言内容': message,
            '发送时间': new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })
        };

        const response = await fetch(`https://formsubmit.co/ajax/${targetEmail}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Referer': 'https://ramanamaharshi.space/'
            },
            body: JSON.stringify(forwardPayload)
        });

        const resText = await response.text();
        let data = {};
        try {
            data = JSON.parse(resText);
        } catch (e) {
            data = { raw: resText };
        }

        // 激活状态提示
        if (data.message && (data.message.includes('needs Activation') || data.message.includes('Activate Form'))) {
            return new Response(JSON.stringify({
                success: true,
                needsActivation: true,
                message: '留言已提交！请站长前往收件邮箱点击激活确认信（仅首次需要），激活后即可正常接收。'
            }), {
                status: 200,
                headers: { 'Content-Type': 'application/json', ...corsHeaders }
            });
        }

        if (response.ok || data.success === 'true' || data.success === true) {
            return new Response(JSON.stringify({ success: true, message: '留言已成功发送，感谢您的支持！' }), {
                status: 200,
                headers: { 'Content-Type': 'application/json', ...corsHeaders }
            });
        }

        return new Response(JSON.stringify({
            success: false,
            message: data.message || '发送未成功，请稍后重试'
        }), {
            status: 200,
            headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
    } catch (err) {
        return new Response(JSON.stringify({ success: false, message: '服务异常，请稍后重试' }), {
            status: 200,
            headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
    }
}

export async function onRequestOptions() {
    return new Response(null, {
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
    });
}
