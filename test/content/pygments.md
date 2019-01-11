title: Pygments Test
date: 2019-01-11
version: 1.0.0
tags: pygments, test

Test the output of Pygments syntax highlighting.

Preformated HTML:

<div class="highlight">
<pre>
<span class="kn">import</span> <span class="nn">pika</span>

<span class="k">class</span> <span class="nc">MessageQueueService</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>

    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">,</span> <span class="n">queue</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">direction</span><span class="o">=</span><span class="n">MessageQueueLog</span><span class="o">.</span><span class="n">RECEIVED</span><span class="p">):</span>
        <span class="n">message_log</span> <span class="o">=</span> <span class="n">MessageQueueLog</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
                <span class="n">queue</span><span class="o">=</span><span class="n">queue</span><span class="p">,</span>
                <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
                <span class="n">message</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
                <span class="n">direction</span><span class="o">=</span><span class="n">direction</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">message_log</span>
<span class="o">...</span>
</pre>
</div>

From Markdown code section:

~~~java
import pika

    class MessageQueueService(object):

        def log(self, message, queue, host, direction=MessageQueueLog.RECEIVED):
            message_log = MessageQueueLog.objects.create(
                    queue=queue,
                    host=host,
                    message=message,
                    direction=direction
                )
            return message_log
    ...
~~~
