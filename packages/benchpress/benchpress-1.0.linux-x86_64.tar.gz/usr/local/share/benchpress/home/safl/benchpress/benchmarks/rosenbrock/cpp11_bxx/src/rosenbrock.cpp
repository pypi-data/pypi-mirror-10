#include <iostream>
#include <iomanip>
#include <bp_util.h>
#include <bxx/bohrium.hpp>

using namespace std;
using namespace bxx;

double rosenbrock(multi_array<double>& x)
{
    return scalar<double>(sum(
        pow(1.0-x[_(0,-2)], 2.0) + \
        100.0 * pow(x[_(1,-1)]-pow(x[_(0,-2)], 2.0), 2.0)
    ));
}

int main(int argc, char* argv[])
{
    bp_util_type bp = bp_util_create(argc, argv, 2);// Grab arguments
    if (bp.args.has_error) {
        return 1;
    }
    const int nelements = bp.args.sizes[0];
    const int trials = bp.args.sizes[1];

    multi_array<double> dataset;                    // Create pseudo-data
    dataset = range<double>(nelements) / (double)nelements;

    bp.timer_start();                               // Start timer
    double res = 0.0;
    for(int i=0; i<trials; ++i) {
        res = rosenbrock(dataset);                  // Run benchmark
    }
    bp.timer_stop();                                // Stop timer
    bp.print("rosenbrock(cpp11_bxx)");
    if (bp.args.verbose) {                          // ..and value.
        cout << fixed << setprecision(11)
			 << "Result = " << res << endl;
    }

    return 0;
}
