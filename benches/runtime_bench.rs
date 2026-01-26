use criterion::{BatchSize, Criterion, PlotConfiguration, criterion_group, criterion_main};
use std::hint::black_box;
use std::vec::Vec;

fn runtime_bench(c: &mut Criterion) {
    // setup benchmark group
    let mut meas: std::vec::Vec<std::time::Duration> = Vec::with_capacity(1000);
    let mut bench = c.benchmark_group("runtime_bench");
    let plot = PlotConfiguration::default().summary_scale(criterion::AxisScale::Logarithmic);
    bench.plot_config(plot);

    // run test
    bench.bench_function("runtime_bench", |b| {
        b.iter_batched(
            || {},
            |_| {
                let start = std::time::Instant::now();
                black_box(mte_201::fast_fft());

                meas.push(start.elapsed())
            },
            BatchSize::NumIterations(5000),
        );
    });

    // signals end
    bench.finish();

    // print result summary
    println!(
        "Average runtime: {:?}, sample size: {:?}",
        meas.iter().sum::<std::time::Duration>() / (meas.len() as u32),
        meas.len()
    );

    // print results for later analysis
    meas.iter().for_each(|d| {
        println!("{:?}", d);
    });
}

criterion_group!(name = benches; config = Criterion::default().sample_size(10); targets = runtime_bench);
criterion_main!(benches);
