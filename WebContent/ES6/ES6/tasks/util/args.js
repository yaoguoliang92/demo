import yargs from 'yargs';

const args = yargs

    //开发环境  线下线上
    .option('production',{
        boolean:true,
        default:false,
        describe:'min all scripts'
    })
    //改了东西要不要自动编译
    .option('watch',{
        boolean:true,
        default:false,
        describe:'watch all files'
    })

    //输出详细的日志
    .option('verbose',{
        boolean:true,
        default:false,
        describe:'log'
    })

    //映射 sourcemap
    .option('sourcemap',{
        describe:'force the creation of souceamp'
    })

    //端口
    .option('port',{
        string:true,
        default:8080,
        describe:'log'
    })
    //表示对输入的命令行以字符串内容解析
    .argv
   export default args; 