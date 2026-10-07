# Glossary

This document records the standard terms used throughout the project. Before defining a new term, check that it does not conflict with an existing entry.

## Usage rules

- Introduce concepts using their established English terms.
- After the first mention, use the `Preferred term`.
- Do not substitute synonyms for the same concept without a contextual reason.
- Definitions are explained in more detail in the introductory lesson for each concept.
- Common spoken reading for formulas and symbols is not repeated here; follow the project's style and notation rules.

## Basic mathematics

| Preferred term | English | Avoid or distinguish | Brief meaning | First lesson |
|---|---|---|---|---|
| number | number | Distinguish from a numeral | A mathematical object used to express counts, order, magnitude, and related notions | M00-01 |
| value | value | Distinguish from a symbol | What a number or mathematical object currently represents | M00-01 |
| symbol | symbol | Distinguish from a value | A mark representing a mathematical object | M00-01 |
| absolute value | absolute value | Distinguish from a signed value | A real number's distance from 0, irrespective of its sign | M01-03 |
| variable | variable | Not always an unknown | A symbol whose value can vary | M00-01 |
| constant | constant | A fixed value | An object whose value does not change within the context | M00-01 |
| parameter | parameter | Not constant in every context | A value that a model adjusts through learning | M00-01 |
| hyperparameter | hyperparameter | Distinguish from a parameter | A setting chosen or searched outside the learning procedure | M00-01 |
| input | input | Distinguish from a parameter | Data supplied to a model or function | M00-01 |
| output | output | Distinguish from an input | The result computed by a model or function | M00-01 |
| expression | expression | Distinguish from an equation | A combination of numbers and operations | M00-02 |
| equality | equality | Distinguish from an equation | A proposition that two expressions are equal | M00-02 |
| left-hand side | left-hand side, LHS | Not limited to one term on the left | The entire expression to the left of the equality sign | M00-02 |
| right-hand side | right-hand side, RHS | Not limited to one term on the right | The entire expression to the right of the equality sign | M00-02 |
| equation | equation | Distinguish from equalities in general | An equality whose truth depends on the values of its unknowns | M00-02 |
| solution | solution | Distinguish from computation results in general | A value that makes an equation or condition true | M00-02 |
| identity | identity | Distinguish from an equality holding only at particular values | An equality holding for every permitted value of its variables | M00-02 |
| function | function | Do not equate with a formula | A rule assigning outputs to inputs | M00-03 |
| function value | function value | Distinguish from the function itself | The output obtained by applying a function to a particular input | M00-03 |
| domain | domain | The input set | The set of objects a function accepts as inputs | M00-03 |
| codomain | codomain | Distinguish from the range | The designated set to which a function's outputs belong | M00-03 |
| range | image, range | Distinguish from the codomain | The set of outputs actually attained | M00-03 |
| coordinate | coordinate | Distinguish from the point itself | A value describing a point's position relative to reference axes | M00-04 |
| ordered pair | ordered pair | Distinguish from a set, which does not preserve order | A pair of values preserving the roles of the first and second entries | M00-04 |
| coordinate plane | coordinate plane | Distinguish from a function's domain | A plane on which two coordinate axes describe point positions | M00-04 |
| graph | graph | Distinguish contextually from a graph data structure | An object representing a function's inputs and outputs as coordinate points | M00-04 |
| intercept | intercept | Distinguish from slope | Where a graph meets a coordinate axis | M00-04 |
| exponent | exponent | Distinguish from an exponential function | A value extending the number of repeated multiplications of a base | M00-05 |
| base | base | Distinguish from the input to a logarithm | The reference number for powers and logarithms | M00-05 |
| exponential function | exponential function | Distinguish from a power function | A function $a^x$ with its input in the exponent | M00-05 |
| logarithm | logarithm | Not restricted to the natural logarithm | A function giving the power to which the base must be raised to obtain the input | M00-05 |
| natural logarithm | natural logarithm | Distinguish from the common logarithm with base 10 | The logarithm with base $e$ | M00-05 |
| index | index | Distinguish from the value itself | A subscript distinguishing the positions or roles of multiple objects | M00-06 |
| summation | summation | Distinguish contextually from a single addition | An operation adding terms over a specified range | M00-06 |
| product notation | product notation | Distinguish from the product rule | Notation for multiplying terms over a specified range | M01-07 |
| dummy index | dummy index | Distinguish from a free index | An index that varies only within a sum and can be renamed | M00-06 |
| arithmetic mean | arithmetic mean | Distinguish from the median | The sum of values divided by their count | M00-06 |
| weighted sum | weighted sum | Distinguish from the arithmetic mean | A sum obtained by multiplying each term by its weight | M00-06 |
| set | set | Distinguish from a sequence | A collection of distinguishable objects as elements | M00-07 |
| element | element | Distinguish from a subset | An individual object belonging to a set | M00-07 |
| subset | subset | Distinguish from membership | A relation in which every element of one set also belongs to another | M00-07 |
| empty set | empty set | Distinguish from a set containing the empty set | A set with no elements | M00-07 |
| union | union | Distinguish from intersection | The set of elements belonging to at least one of two sets | M00-07 |
| intersection | intersection | Distinguish from union | The set of elements belonging to both sets | M00-07 |
| proposition | proposition | Distinguish from a condition with an unspecified value | A statement that can be judged true or false | M00-07 |
| implication | implication | Do not equate with causation | A logical relation in which the truth of one proposition entails the truth of another | M00-07 |
| necessary condition | necessary condition | Distinguish from a sufficient condition | A condition required for a conclusion or property to hold | M00-07 |
| sufficient condition | sufficient condition | Distinguish from a necessary condition | A condition whose satisfaction guarantees a conclusion or property | M00-07 |
| counterexample | counterexample | Distinguish from merely a different example | A case that makes a universal proposition false | M00-07 |
| composition | composition | Distinguish from a product of functions | Feeding the output of one function into another | M00-08 |
| identity function | identity function | Distinguish from a constant function | A function returning its input unchanged | M00-08 |
| inverse function | inverse function | Distinguish from the reciprocal of a function value | A function taking an output back to its original input | M00-08 |
| injective function | injective function | Distinguish from a surjective function | A function sending distinct inputs to distinct outputs | M00-08 |
| surjective function | surjective function | Distinguish from an injective function | A function attaining every element of its codomain | M00-08 |
| bijective function | bijective function | Distinguish from a function satisfying only injectivity or only surjectivity | A function that is both injective and surjective | M00-08 |
| scalar | scalar | A number | A value expressed as a single magnitude | M00-09 |
| vector | vector | Do not equate with a mere list | An element of a vector space | M00-09 |
| component | component | Distinguish from the entire vector | An individual value in a vector's coordinate representation | M02-01 |
| zero vector | zero vector | Distinguish from the scalar 0 | A vector with every component equal to 0 | M02-01 |
| vector addition | vector addition | Distinguish contextually from scalar addition | Adding corresponding components of vectors with the same dimension | M02-01 |
| scalar multiplication | scalar multiplication | Distinguish from the inner product of two vectors | Multiplying every component of a vector by the same scalar | M02-01 |
| additive inverse | additive inverse | Distinguish from a reciprocal | A vector whose sum with the original vector is the zero vector | M02-01 |
| matrix | matrix | Do not equate with a table | A coordinate representation of a linear map or an array of numbers | M00-09 |
| shape | shape, tensor shape | Distinguish contextually from dimension | A tuple listing the lengths of an array's or tensor's axes in order | M00-09 |
| dimension | dimension | Distinguish from a vector's norm | The number of independent coordinates or components of a vector | M00-09 |
| transpose | transpose | Distinguish from a matrix inverse | An operation interchanging rows and columns | M00-09 |
| inner product | inner product, dot product | Distinguish from an elementwise product | An operation mapping two vectors of the same dimension to a scalar | M00-09 |
| norm | norm | Distinguish from dimension | A scalar expressing a vector's magnitude | M00-09 |
| affine layer | affine layer | Distinguish from a layer performing only a linear transformation | A layer that multiplies by a weight matrix and then adds a bias | M00-09 |
| weight | weight | Connect contextually to coefficients in a weighted sum | A parameter determining how input components contribute to an output | M00-09 |
| bias | bias | Distinguish contextually from statistical bias | A parameter added to the result of a linear transformation | M00-09 |

## Calculus

| Preferred term | English | Avoid or distinguish | Brief meaning | First lesson |
|---|---|---|---|---|
| change | change, increment | Distinguish from the final value | The final value minus the initial value | M01-01 |
| average rate of change | average rate of change | Distinguish from the mean of two function values | The ratio of output change to input change | M01-01 |
| slope | slope | Distinguish contextually from a gradient | Vertical change divided by horizontal change in a coordinate plane | M01-01 |
| secant line | secant line | Distinguish from a tangent line | A line through two distinct points on a curve | M01-01 |
| limit | limit | Distinguish from the function value | A value approached by the output as the input approaches a given value | M01-02 |
| left-hand limit | left-hand limit | Distinguish from a right-hand limit | A limit as the input approaches a value from below | M01-02 |
| right-hand limit | right-hand limit | Distinguish from a left-hand limit | A limit as the input approaches a value from above | M01-02 |
| continuity | continuity | Not equivalent to differentiability | The property that a limit and the function value agree at a point | M01-02 |
| differentiation | differentiation | Distinguish contextually from a derivative | The process of finding a local rate of change | M01-03 |
| derivative at a point | derivative at a point | Distinguish from the derivative function | An instantaneous rate of change obtained as the limit of average rates at a point | M01-03 |
| derivative | derivative | Distinguish contextually from differentiation | A function giving the rate of change at each point | M01-03 |
| tangent line | tangent line | Distinguish from a secant line | A line expressing the local direction of a curve at a point | M01-03 |
| differentiable | differentiable | Not equivalent to continuous | Describes a function whose change admits a linear approximation with error negligible relative to the input change | M01-03 |
| critical point | critical point | Not equivalent to an extremum | A point in the domain where the derivative is 0 or does not exist | M01-04 |
| stationary point | stationary point | Distinguish from critical points in general | A point where the derivative is 0 | M01-04 |
| local maximum | local maximum | Distinguish from a global maximum | The largest function value within a neighborhood of a point | M01-04 |
| local minimum | local minimum | Distinguish from a global minimum | The smallest function value within a neighborhood of a point | M01-04 |
| sum rule | sum rule | Distinguish from the product rule | A rule for differentiating a sum of functions term by term | M01-05 |
| product rule | product rule | Distinguish from a product of derivatives | The differentiation rule $(uv)'=u'v+uv'$ | M01-05 |
| quotient rule | quotient rule | Distinguish from a quotient of derivatives | A rule for differentiating a quotient that also accounts for changes in the denominator | M01-05 |
| power rule | power rule | Distinguish from differentiating an exponential function | The rule differentiating $x^n$ to $nx^{n-1}$ | M01-05 |
| chain rule | chain rule | Distinguish from the product rule | A rule multiplying local derivatives along a composition path | M01-06 |
| local derivative | local derivative | Distinguish from the derivative of the entire path | The derivative of one computational step's output with respect to its input | M01-06 |
| log-sum-exp | log-sum-exp | Distinguish from softmax | A function taking the logarithm of a sum of exponentials | M01-07 |
| Riemann sum | Riemann sum | Distinguish from the limiting value of a definite integral | An approximation summing products of function values and small interval widths | M01-08 |
| definite integral | definite integral | Distinguish from an indefinite integral | A scalar accumulating signed function values over an interval | M01-08 |
| integrand | integrand | Distinguish from the result of integration | The function accumulated inside an integral | M01-08 |
| variable of integration | variable of integration | Distinguish from integration endpoints | The input variable along which small intervals are partitioned | M01-08 |
| interval additivity | interval additivity | Distinguish from adding function values | The property that integrals over adjacent intervals sum to the integral over their union | M01-08 |
| accumulation function | accumulation function | Distinguish from the integrand | A function whose input is an integration endpoint | M01-08 |
| fundamental theorem of calculus | fundamental theorem of calculus | Distinguish from a single differentiation rule | A theorem connecting differentiation of an accumulation function to evaluation of definite integrals using antiderivatives | M01-09 |
| antiderivative | antiderivative | Distinguish from a derivative | A function whose derivative is the given function | M01-09 |
| indefinite integral | indefinite integral | Distinguish from a definite integral | The family of all antiderivatives, including a constant of integration | M01-09 |
| constant of integration | constant of integration | Distinguish from an integration endpoint | A value representing the constant difference between antiderivatives in an indefinite integral | M01-09 |
| net change theorem | net change theorem | Distinguish from total distance traveled | A theorem expressing the definite integral of a rate as the difference between endpoint function values | M01-09 |
| partial derivative | partial derivative | Distinguish from the total derivative | A rate of change with the other inputs held fixed | M01-10 |
| partial derivative at a point | partial derivative at a point | Distinguish from the partial derivative function | An instantaneous rate measured along one coordinate direction at a point | M01-10 |
| partial derivative function | partial derivative function | Distinguish from a partial derivative at a point | A function assigning each input point its partial derivative along one coordinate direction | M01-10 |
| directional derivative | directional derivative | Distinguish from a gradient | A rate of change in a specified direction | M01-11 |
| gradient | gradient | Distinguish from the slope of a graph | A vector representation of directional derivatives | M01-11 |
| unit vector | unit vector | Distinguish from a vector of arbitrary length with the same direction | A vector with norm 1 | M01-11 |
| gradient descent | gradient descent | Distinguish from gradient computation | A method updating parameters opposite to the loss gradient | M01-11 |
| saddle point | saddle point | Distinguish from a local minimum | A stationary point with both larger and smaller values nearby | M01-11 |
| Taylor approximation | Taylor approximation | Distinguish from an exact equality | A polynomial approximation to nearby function values using derivatives at a point | M01-12 |
| second derivative | second derivative | Distinguish from the first derivative | The function obtained by differentiating the derivative once more | M01-12 |
| remainder | remainder | Distinguish contextually from a regression residual | The difference between the actual function value and the Taylor polynomial | M01-12 |
| numerical differentiation | numerical differentiation | Distinguish from analytic differentiation | Approximating a derivative using finite differences of nearby function values | M01-13 |
| forward difference | forward difference | Distinguish from a central difference | A rate approximation using the current point and a point ahead | M01-13 |
| backward difference | backward difference | Distinguish from a central difference | A rate approximation using a point behind and the current point | M01-13 |
| central difference | central difference | Distinguish from a one-sided difference | A rate approximation using symmetric points on either side of the reference point | M01-13 |
| truncation error | truncation error | Distinguish from roundoff error | Error caused by discarding higher-order terms in an approximation | M01-13 |
| roundoff error | roundoff error | Distinguish from truncation error | Error arising from finite-precision number representations and arithmetic | M01-13 |
| gradient check | gradient check | Distinguish from evaluating learning performance | Comparing analytic or automatic-differentiation gradients with numerical differences | M01-13 |
| integration | integration | Not limited to area | Continuous accumulation of small quantities | M01-08 |
| total derivative | total derivative | Distinguish from a list of partial derivatives | A local linear map taking input-change vectors to first-order output changes | M03-10 |
| remainder | remainder | Distinguish from the first-order term | The error obtained by subtracting the approximation from the actual function change | M03-10 |
| little-o | little-o notation | Distinguish from a fixed small constant | An error order whose ratio to a reference quantity tends to 0 in the limit | M03-10 |
| local linearization | local linearization | Distinguish from global linearity | Approximating function changes near a reference point using the derivative | M03-10 |
| Jacobian | Jacobian | Distinguish from a gradient column vector | The coordinate matrix of a vector function's total derivative, with output rows and input columns | M03-11 |
| local sensitivity | local sensitivity | Distinguish from global stability | The rate of output change in response to small input changes near a reference point | M03-11 |
| Hessian | Hessian | Distinguish from the activation matrix H | A matrix of second partial derivatives, the Jacobian of a scalar function's gradient | M03-12 |
| second differential | second differential | Distinguish from the Hessian coordinate matrix | A bilinear form mapping two change vectors to a second-order change | M03-12 |
| mixed partial derivative | mixed partial derivative | Distinguish from differentiating twice with respect to the same variable | A derivative taken successively with respect to different input coordinates | M03-12 |
| HVP | Hessian-vector product | Distinguish from the full Hessian | The result of multiplying a Hessian by one direction vector | M03-12 |
| Hessian spectrum | Hessian spectrum | Distinguish from one eigenvalue or the global loss landscape | The eigenvalues of a Hessian computed at one parameter point | M03-12 |
| JVP | Jacobian-vector product | Distinguish from the full Jacobian | A Jacobian-vector product mapping an input tangent to an output tangent | M03-13 |
| VJP | vector-Jacobian product | Distinguish its direction from a JVP | A product of the transposed Jacobian and a vector pulling an output cotangent back to the input | M03-13 |
| tangent | tangent | Distinguish from the original input value | A first-order change propagated along a specified input direction | M03-13 |
| cotangent | cotangent | Distinguish from an output perturbation | A dual value pulling the sensitivity of a scalar measurement back to the input | M03-13 |
| adjoint identity | adjoint identity | Does not say that a JVP and a VJP are the same vector | An equality between the scalar pairings of a JVP and a VJP | M03-13 |
| automatic differentiation | automatic differentiation, AD | Distinguish from numerical differentiation | Composing differentiation rules for elementary operations through an executed computation | M03-14 |
| computational graph | computational graph | Distinguish from a function graph | A graph of directed dependencies between values and operations | M03-14 |
| forward mode | forward-mode AD | Distinguish from the model's forward pass itself | An AD mode propagating primal values and tangents in computation order | M03-14 |
| reverse mode | reverse-mode AD | Distinguish from computing an inverse function | An AD mode propagating cotangents in reverse operation order | M03-14 |
| local derivative | local derivative | Distinguish from the derivative of the entire composition | The derivative between the input and output of one elementary operation | M03-14 |
| gradient accumulation | gradient accumulation | Distinguish from an optimizer update | Adding cotangent contributions from multiple computational paths | M03-14 |
| checkpointing | checkpointing | Distinguish from saving a model checkpoint | Reducing reverse-mode memory by recomputing some intermediate values | M03-14 |

## Linear algebra

| Preferred term | English | Avoid or distinguish | Brief meaning | First lesson |
|---|---|---|---|---|
| vector space | vector space | Not restricted to sets of numerical column vectors | A set whose vector addition and scalar multiplication satisfy the axioms | M03-01 |
| vector space axioms | vector space axioms | Distinguish from computational shortcuts | Algebraic laws that addition and scalar multiplication must satisfy | M03-01 |
| function space | function space | Distinguish from a single function | A vector space of functions with specified inputs, outputs, and conditions | M03-01 |
| ordered basis | ordered basis | Distinguish from a basis set without order | An ordered list of basis vectors that also fixes coordinate positions | M03-02 |
| linear map | linear map | Distinguish from its matrix representation | A function between two vector spaces preserving linear combinations | M03-02 |
| matrix representation | matrix representation | Distinguish from the abstract linear map | A linear map's coordinate matrix after choosing domain and codomain bases | M03-02 |
| identity map | identity map | Distinguish from an identity matrix | A map sending each vector to itself | M03-02 |
| change-of-basis matrix | change-of-basis matrix | Distinguish from a transformation changing the vector itself | An invertible matrix converting coordinates in one basis to coordinates in another | M03-03 |
| similarity transformation | similarity transformation | Distinguish from a congruence transformation | A transformation relating the matrices of the same linear operator in different bases | M03-03 |
| coordinate dependence | coordinate dependence | Distinguish from a change to the object itself | The dependence of numerical representations on the choice of basis | M03-03 |
| passive change of coordinates | passive change of coordinates | Distinguish from an active transformation | Keeping an object fixed while changing only its coordinate representation | M03-03 |
| active transformation | active transformation | Distinguish from a passive change of coordinates | A map changing the vector itself while keeping the coordinate system fixed | M03-03 |
| invariant | invariant | Distinguish from an unconditional claim of being unchanged | A function or quantity preserved under specified transformations | M03-04 |
| invariance | invariance | Distinguish from equivariance | The property that transforming an input leaves the output unchanged | M03-04 |
| equivariance | equivariance | Distinguish from invariance | The property that outputs change in a specified way corresponding to input transformations | M03-04 |
| sum of subspaces | sum of subspaces | Distinguish from a union | A subspace formed by adding vectors chosen from two subspaces | M03-05 |
| direct sum | direct sum | Distinguish from sums of subspaces in general | A sum of subspaces whose intersection contains only the zero vector and whose decomposition is unique | M03-05 |
| complement | complement | Distinguish from a set-theoretic complement | A subspace whose direct sum with the given subspace is the entire space | M03-05 |
| orthogonal complement | orthogonal complement | Distinguish from a general complement | The space of vectors orthogonal to every vector in a given subspace | M03-05 |
| equivalence relation | equivalence relation | Distinguish from similarity | A relation satisfying reflexivity, symmetry, and transitivity | M03-06 |
| equivalence class | equivalence class | Distinguish from one representative | The set of all elements equivalent to a given element | M03-06 |
| representative | representative | Distinguish from the equivalence class itself | One element chosen to represent an equivalence class | M03-06 |
| coset | coset | Distinguish from the subspace itself | A set obtained by translating a subspace by a vector | M03-06 |
| quotient space | quotient space | Distinguish from scalar division | A vector space of equivalence classes ignoring differences along a subspace | M03-06 |
| quotient map | quotient map | Distinguish from an orthogonal projection | A linear map sending a vector to its coset | M03-06 |
| well-defined | well-defined | Distinguish from a rule depending on the representative chosen | Describes a rule giving consistent results for all permitted representations | M03-06 |
| coefficient | coefficient | Distinguish from a vector component | A scalar multiplying a vector in a linear combination | M02-02 |
| linear combination | linear combination | Distinguish from a simple sum | A sum of vectors multiplied by scalars | M02-02 |
| span | span | Do not confuse with a range | The set of all possible linear combinations | M02-02 |
| subspace | subspace | Distinguish from a subset | A set containing the zero vector and closed under vector addition and scalar multiplication | M02-02 |
| Euclidean distance | Euclidean distance | Distinguish from dimension | The Euclidean norm of the difference between two vectors | M02-03 |
| orthogonal | orthogonal | Distinguish from statistically independent | Describes vectors whose inner product is 0 | M02-03 |
| orthogonal projection | orthogonal projection | Distinguish from arbitrary coordinate deletion | An operation sending a vector to its nearest vector in a specified subspace | M02-03 |
| cosine similarity | cosine similarity | Distinguish from Euclidean distance | The cosine of the angle between two nonzero vectors | M02-03 |
| matrix multiplication | matrix multiplication | Distinguish from an elementwise product | A matrix formed from inner products of left-hand rows and right-hand columns | M02-04 |
| identity matrix | identity matrix | Distinguish from a matrix of all ones | A square matrix leaving the vector or matrix it multiplies unchanged | M02-04 |
| Hadamard product | Hadamard product | Distinguish from matrix multiplication | Multiplying corresponding entries of matrices with the same shape | M02-04 |
| linear transformation | linear transformation | Distinguish from an affine transformation | A transformation preserving vector addition and scalar multiplication | M02-05 |
| standard basis | standard basis | Distinguish from an arbitrary basis | A basis of vectors with one component equal to 1 and all others equal to 0 | M02-05 |
| affine transformation | affine transformation | Distinguish from a linear transformation | A transformation adding a fixed vector to the result of a linear transformation | M02-05 |
| augmented matrix | augmented matrix | Distinguish from enlarging a matrix | A matrix adjoining a system's right-hand side to its coefficient matrix | M02-06 |
| elementary row operation | elementary row operation | Distinguish from a column operation | Swapping, scaling, or adding rows while preserving the solution set | M02-06 |
| Gaussian elimination | Gaussian elimination | Do not equate with computing an inverse matrix | Solving a system of equations through elementary row operations | M02-06 |
| pivot | pivot | Distinguish from merely a large entry | The position of a row's first nonzero entry in row-echelon form | M02-06 |
| free variable | free variable | Distinguish from arbitrary error | A freely chosen variable corresponding to a column without a pivot | M02-06 |
| inverse matrix | inverse matrix | Distinguish from entrywise reciprocals | A matrix whose product with the original matrix in either order is the identity | M02-06 |
| invertible matrix | invertible matrix | Distinguish from square matrices in general | A square matrix with an inverse | M02-06 |
| singular matrix | singular matrix | Distinguish from the ordinary meaning of unusual | A square matrix with no inverse | M02-06 |
| linear dependence | linear dependence | Not restricted to vectors being identical | A relation admitting coefficients, not all zero, whose vector combination is the zero vector | M02-07 |
| coordinate vector | coordinate vector | Distinguish from the vector itself | A column of coefficients representing a vector in a chosen basis | M02-07 |
| linear independence | linear independence | Not equivalent to orthogonality | A relation in which no vector can be formed as a linear combination of the others | M02-07 |
| basis | basis | Not equivalent to coordinate axes | An independent spanning set giving unique representations of the space | M02-07 |
| kernel | kernel, null space | Distinguish from a convolution kernel | The inputs that a linear map sends to 0 | M02-08 |
| image | image | Distinguish from image data | The outputs actually produced by a linear map | M02-08 |
| rank | rank | Distinguish from a coefficient or ranking | The number of independent output directions | M02-08 |
| column space | column space | Distinguish from row space | The image spanned by a matrix's column vectors | M02-08 |
| nullity | nullity | Distinguish from the kernel itself | The dimension of the kernel | M02-08 |
| rank-nullity theorem | rank-nullity theorem | Does not assert that rank equals nullity | The theorem that input dimension equals rank plus nullity | M02-08 |
| orthogonal basis | orthogonal basis | Distinguish from an orthonormal basis | A basis of mutually orthogonal vectors | M02-09 |
| orthonormal basis | orthonormal basis | Distinguish from a merely orthogonal basis | A basis of mutually orthogonal vectors, each with norm 1 | M02-09 |
| Kronecker delta | Kronecker delta | Distinguish from the Dirac delta | A symbol equal to 1 when two indices agree and 0 otherwise | M02-09 |
| projection matrix | projection matrix | Distinguish from an arbitrary dimension-reduction matrix | A matrix orthogonally projecting vectors onto a specified subspace | M02-09 |
| idempotent matrix | idempotent matrix | Distinguish from an identity matrix | A matrix satisfying $\mathbf P^2=\mathbf P$ | M02-09 |
| Gram-Schmidt process | Gram-Schmidt process | Distinguish from row elimination | Converting independent vectors to an orthonormal basis of the same span | M02-09 |
| least squares | least squares | Distinguish from solving equations exactly | Minimizing the squared norm of a residual | M02-09 |
| normal equations | normal equations | Unrelated to normality of a probability distribution | Equations obtained from the orthogonality condition on a least-squares residual | M02-09 |
| determinant | determinant | Distinguish from the product of all matrix entries | The oriented volume scale factor of a square matrix | M02-10 |
| orientation | orientation | Distinguish from a single vector direction | Whether the ordering of basis axes is preserved or reversed | M02-10 |
| triangular matrix | triangular matrix | Distinguish from a diagonal matrix | A square matrix with all entries on one side of the main diagonal equal to 0 | M02-10 |
| eigenvalue | eigenvalue | Distinguish from a singular value | A scaling coefficient along an eigendirection | M02-11 |
| eigenvector | eigenvector | Distinguish from a singular vector | A vector whose direction is preserved by a linear transformation | M02-11 |
| eigenspace | eigenspace | Distinguish from one eigenvector | The subspace comprising eigenvectors for one eigenvalue and the zero vector | M02-11 |
| characteristic polynomial | characteristic polynomial | Distinguish from the minimal polynomial | The polynomial $\det(\mathbf A-\lambda\mathbf I)$ defining the eigenvalue equation | M02-11 |
| diagonalization | diagonalization | Distinguish from reading only diagonal entries | A decomposition expressing a matrix as a diagonal matrix in an eigenvector basis | M02-11 |
| symmetric matrix | symmetric matrix | Distinguish from a matrix whose entries are all equal | A square matrix equal to its transpose | M02-12 |
| spectral theorem | spectral theorem | Does not apply to all square matrices | A theorem guaranteeing an orthonormal eigenbasis for a real symmetric matrix | M02-12 |
| spectral decomposition | spectral decomposition | Distinguish from SVD | A decomposition expressing a symmetric matrix as $\mathbf Q\boldsymbol\Lambda\mathbf Q^\top$ | M02-12 |
| quadratic form | quadratic form | Distinguish from a bilinear form | A scalar expression of the form $\mathbf x^\top\mathbf A\mathbf x$ | M02-12 |
| positive semidefinite | positive semidefinite, PSD | Distinguish from positive definite | Describes a quadratic form nonnegative for every vector | M02-12 |
| singular value decomposition | singular value decomposition, SVD | Distinguish from eigendecomposition | A decomposition into input directions, amplification factors, and output directions | M02-13 |
| singular value | singular value | Distinguish from an eigenvalue | A nonnegative amplification factor along a right singular direction | M02-13 |
| right singular vector | right singular vector | Distinguish from a left singular vector | An orthogonal input-space direction in an SVD | M02-13 |
| left singular vector | left singular vector | Distinguish from a right singular vector | An orthogonal output-space direction in an SVD | M02-13 |
| compact SVD | compact SVD | Distinguish from full SVD | An SVD retaining only components associated with positive singular values | M02-13 |
| spectral norm | spectral norm | Distinguish from the Frobenius norm | A matrix's largest directional amplification factor | M02-13 |
| Frobenius norm | Frobenius norm | Distinguish from the spectral norm | The square root of the sum of squared matrix entries or squared singular values | M02-13 |
| truncated SVD | truncated SVD | Distinguish from compact SVD | A low-rank approximation retaining only the leading singular components | M02-13 |
| centering | centering | Distinguish from standardization | Preprocessing that subtracts each feature's sample mean | M02-14 |
| covariance matrix | covariance matrix | Distinguish from a correlation matrix | A symmetric matrix of sample covariances between feature pairs | M02-14 |
| trace | trace | Distinguish from the determinant | The sum of a square matrix's diagonal entries | M02-14 |
| principal component | principal component | Distinguish from one original feature | An orthogonal direction with large variance in centered data | M02-14 |
| principal component score | principal component score | Distinguish from a principal component direction | A coordinate obtained by projecting a sample onto a principal component direction | M02-14 |
| explained variance ratio | explained variance ratio | Do not equate with overall reconstruction accuracy | The proportion of total sample variance accounted for by a principal component | M02-14 |
| standardization | standardization | Distinguish from centering | Preprocessing that subtracts each feature's mean and divides by its standard deviation | M02-14 |
| principal component analysis | principal component analysis, PCA | Not equivalent to SVD | A method finding orthogonal directions with large data variation | M02-14 |
| L1 norm | L1 norm | Distinguish from the Euclidean norm | The sum of absolute values of vector components | M02-15 |
| L2 norm | L2 norm | Distinguish from the L1 norm | The square root of the sum of squared vector components | M02-15 |
| infinity norm | infinity norm | Does not mean infinite magnitude | The maximum absolute value among vector components | M02-15 |
| triangle inequality | triangle inequality | Do not interpret as an equality | The condition that the norm of a sum is no greater than the sum of the norms | M02-15 |
| condition number | condition number | Distinguish from the determinant | The ratio of the largest to the smallest directional amplification factor | M02-15 |
| relative error | relative error | Distinguish from absolute error | The error norm divided by the norm of a reference value | M02-15 |
| dual space | dual space | Distinguish from the original space | The space of linear functions mapping vectors to scalars | M03-07 |
| covector | covector | Distinguish from a gradient vector | A linear function acting on a vector to produce a scalar | M03-07 |
| dual basis | dual basis | Distinguish from the original basis | A covector basis reading individual coordinate coefficients in the original basis | M03-07 |
| differential | differential | Distinguish from a gradient vector | A covector mapping a change vector to a first-order change in a function value | M03-07 |
| bilinear map | bilinear map | Distinguish from a linear function of the paired inputs | A function linear in each of its two inputs separately | M03-08 |
| bilinear form | bilinear form | Do not equate with an inner product | A bilinear map sending two vectors in the same vector space to a scalar | M03-08 |
| symmetric part | symmetric part | Distinguish from the entire original matrix | The symmetric matrix $\frac12(\mathbf A+\mathbf A^\top)$ | M03-08 |
| congruence transformation | congruence transformation | Distinguish from a similarity transformation | The transformation $\mathbf P^\top\mathbf A\mathbf P$ relating a bilinear form's matrices in different bases | M03-08 |
| polarization identity | polarization identity | Distinguish from the quadratic form itself | A formula recovering a bilinear form from a symmetric quadratic form | M03-08 |
| tensor | tensor | Not exactly equivalent to a multiaxis array | An object with multilinear structure and a basis-transformation law | M00-09 |
| multilinear map | multilinear map | Distinguish from a linear function of all inputs jointly | A function linear in each input slot separately | M03-09 |
| tensor order | tensor order | Distinguish from tensor rank | The number of a tensor's vector and covector input slots | M03-09 |
| tensor product | tensor product | Distinguish from an elementwise product | An operation combining multilinear input slots to form a new tensor | M03-09 |
| outer product | outer product | Distinguish from an inner product | A product of two coordinate columns forming a rank-1 matrix or an order-2 component array | M03-09 |
| contraction | contraction | Distinguish from an arbitrary sum of entries | Reducing tensor order by summing matching indices or supplying an input | M03-09 |
| tensor rank | tensor rank | Distinguish from tensor order | A concept concerning the minimum number of rank-1 tensor terms needed to express a tensor | M03-09 |
| reparameterization | reparameterization | Do not equate with changing the model function | Expressing the same model family through a different parameter map | M03-15 |
| model symmetry | model symmetry | Distinguish from arbitrary parameter changes | The property of changing parameters while preserving the model function on every input | M03-15 |
| symmetry transformation | symmetry transformation | Distinguish from a passive change of coordinates | An active parameter transformation preserving the model function | M03-15 |
| orbit | orbit | Distinguish from an optimization trajectory | The set obtained by applying all permitted symmetry transformations to an object | M03-15 |
| functional equivalence | functional equivalence | Distinguish from equal outputs on a finite sample | A relation in which two parameterizations have identical output functions on every permitted input | M03-15 |
| hidden-unit permutation | hidden-unit permutation | Distinguish from moving just one unit | A symmetry permuting hidden units while modifying the adjacent layers together | M03-15 |
| positive scaling symmetry | positive scaling symmetry | Distinguish from negative scaling | A symmetry using ReLU's positive homogeneity to cancel incoming and outgoing weight scales | M03-15 |

## Probability and information

| Preferred term | English | Avoid or distinguish | Brief meaning | First lesson |
|---|---|---|---|---|
| sample space | sample space | Distinguish from a set of observed samples | The set of all outcomes treated as possible by a probability model | M04-01 |
| outcome | outcome | Distinguish from an event | An element of the sample space obtained in one trial | M04-01 |
| event | event | Distinguish from a single outcome | A subset of the sample space to which probability is assigned | M04-01 |
| probability | probability | Distinguish from empirical frequency | An axiomatic rule assigning events numbers in $[0,1]$ | M04-01 |
| complement event | complement event | Distinguish contextually from a set-theoretic complement | The event consisting of outcomes where the event of interest does not occur | M04-01 |
| mutually exclusive | mutually exclusive | Distinguish from independent | Describes two events whose intersection is empty | M04-01 |
| countable additivity | countable additivity | Distinguish from summing probabilities of overlapping events | The axiom that the probability of a union of countably many disjoint events equals the sum of their probabilities | M04-01 |
| inclusion-exclusion | inclusion-exclusion | Distinguish from simply adding probabilities | A formula correcting double counting of intersections in a union's probability | M04-01 |
| empirical frequency | empirical frequency | Distinguish from model probability | The number of event occurrences divided by the number of observations | M04-01 |
| conditional probability | conditional probability | Distinguish from reversing the conditioning direction | The proportion of probability mass assigned to the event of interest within the given event | M04-02 |
| partition | partition | Distinguish from a collection of overlapping subsets | Disjoint events whose union is the sample space | M04-02 |
| law of total probability | law of total probability | Distinguish from one conditional path | A law summing event probabilities contributed by each path of a partition | M04-02 |
| Bayes' rule | Bayes' rule | Distinguish from simply swapping the conditioning direction | A formula computing a posterior from a likelihood and prior | M04-02 |
| prior probability | prior probability | Distinguish from probability after incorporating evidence | The probability of an event of interest before conditioning on new evidence | M04-02 |
| posterior probability | posterior probability | Distinguish from a likelihood | The probability of an event of interest after conditioning on observed evidence | M04-02 |
| base rate | base rate | Distinguish from conditional performance | The underlying proportion of an event of interest in the overall population | M04-02 |
| independence | independence | Distinguish from mutual exclusivity | A relation in which an intersection probability factors into the product of two marginal probabilities | M04-02 |
| conditional independence | conditional independence | Distinguish from unconditional independence | Independence in a distribution with a specified condition held fixed | M04-02 |
| random variable | random variable | Do not equate with a random number | A function mapping outcomes to numbers | M04-03 |
| probability distribution | probability distribution | Distinguish from one observation | A rule by which a random variable assigns probabilities to values or intervals | M04-03 |
| probability mass function | probability mass function, PMF | Distinguish from a probability density function | A function assigning point probabilities to values of a discrete random variable | M04-03 |
| cumulative distribution function | cumulative distribution function, CDF | Distinguish from a probability density function | A function giving the probability that a random variable is at or below a threshold | M04-03 |
| probability density function | probability density function, PDF | Distinguish from probability at one point | A function whose integral over an interval gives a continuous random variable's probability | M04-03 |
| joint distribution | joint distribution | Distinguish from a list of marginal distributions | The probability rule for multiple random variables taking values together | M04-03 |
| marginal distribution | marginal distribution | Distinguish from a conditional distribution | A variable's distribution obtained by summing or integrating out other variables from a joint distribution | M04-03 |
| conditional distribution | conditional distribution | Distinguish from a joint distribution | A probability distribution conditioned on fixed values of other variables | M04-03 |
| preimage | preimage | Distinguish from an inverse function | The set of inputs satisfying a condition on a function's output | M04-03 |
| expectation | expectation | Not always equal to a sample mean | A distribution-weighted mean | M04-04 |
| variance | variance | Distinguish from error | Spread around the mean | M04-04 |
| standard deviation | standard deviation | Distinguish from variance | The square root of variance, measuring spread in the original variable's units | M04-04 |
| indicator variable | indicator variable | Distinguish from the event itself | A random variable equal to 1 if an event occurs and 0 otherwise | M04-04 |
| moment | moment | Distinguish from a power of one observation | The expectation of a power or centered power of a random variable | M04-04 |
| correlation coefficient | correlation coefficient | Distinguish from a causal effect | A summary of linear association obtained by dividing covariance by the product of two standard deviations | M04-04 |
| covariance | covariance | Does not imply causation | A value expressing the linear covariation of two variables | M02-14 |
| support | support | Distinguish from the list of observed values | The set of values a random variable can take | M04-05 |
| Bernoulli distribution | Bernoulli distribution | Distinguish from a binomial distribution | A distribution assigning a success probability to one binary outcome | M04-05 |
| categorical distribution | categorical distribution | Distinguish from a one-hot observation | A distribution assigning probabilities to the selection of one among several categories | M04-05 |
| binomial distribution | binomial distribution | Distinguish from a single Bernoulli trial | The distribution of the number of successes in multiple independent Bernoulli trials | M04-05 |
| Gaussian distribution | Gaussian distribution | Distinguish from an arbitrary distribution with the same mean and variance | A bell-shaped continuous distribution parameterized by mean and variance | M04-05 |
| standard normal distribution | standard normal distribution | Distinguish from a general Gaussian distribution | A Gaussian distribution with mean 0 and variance 1 | M04-05 |
| z-score | z-score | Distinguish from the original observation | The number of standard deviations an observation lies from the mean | M04-05 |
| one-hot vector | one-hot vector | Distinguish from a class probability vector | A vector with 1 at the observed class position and 0 elsewhere | M04-05 |
| multivariate Gaussian | multivariate Gaussian | Do not equate with a collection of independent Gaussian components | A vector distribution specified by a mean vector and covariance matrix | M04-05 |
| population | population | Distinguish from an observed sample | The set of outcomes or distribution to which a researcher intends to generalize | M04-06 |
| sample | sample | Distinguish from a sample space | A finite collection of values observed from a population | M04-06 |
| random sample | random sample | Distinguish from a list of observations | A sample represented by random variables before sampling | M04-06 |
| iid | independent and identically distributed | Distinguish from merely sharing a source | The assumption that observations are independent and follow the same distribution | M04-06 |
| parameter | parameter | Distinguish from a statistic | A fixed unknown value specifying or summarizing a population distribution | M04-06 |
| statistic | statistic | Distinguish from a parameter | A function of a random sample before observation that does not directly take unknown parameters as inputs | M04-06 |
| sample mean | sample mean | Distinguish from a population mean | The statistic obtained by dividing the sum of observations by sample size | M04-06 |
| sample variance | sample variance | Distinguish from population variance | A statistic summarizing squared deviations around the sample mean | M04-06 |
| empirical distribution | empirical distribution | Distinguish from a population distribution | A distribution assigning equal mass to each observed sample value | M04-06 |
| sampling distribution | sampling distribution | Distinguish from a histogram of sample values | The probability distribution of a statistic under repeated sampling | M04-06 |
| standard error | standard error | Distinguish from the standard deviation of raw data | The standard deviation of a statistic's sampling distribution | M04-06 |
| central limit theorem | central limit theorem, CLT | Does not guarantee an exactly Gaussian finite sample | A theorem stating that, under conditions, a standardized sample mean's distribution approaches a Gaussian | M04-06 |
| sampling unit | sampling unit | Not always one observation row | The basic unit independently sampled from a population | M04-06 |
| estimator | estimator | Distinguish from an observed estimate | A statistic mapping a random sample to an estimate of a parameter | M04-07 |
| estimate | estimate | Distinguish from the estimator rule | A fixed value obtained by applying an estimator to an observed sample | M04-07 |
| statistical bias | statistical bias | Distinguish from a neural network bias parameter | The difference between an estimator's expectation and its target parameter | M04-07 |
| unbiased estimator | unbiased estimator | Distinguish from an estimator accurate on every observation | An estimator whose expectation equals its target parameter | M04-07 |
| mean squared error | mean squared error, MSE | Distinguish from variance alone | The expected squared error between an estimator and its target | M04-07 |
| bias-variance tradeoff | bias-variance tradeoff | Distinguish from comparing bias or variance alone | A relation in which allowing bias adjusts variance and overall prediction error | M04-07 |
| shrinkage | shrinkage | Distinguish from arbitrary rescaling | Estimation that draws estimates toward a reference point to reduce variance | M04-07 |
| consistency | consistency | Distinguish from unbiasedness | The property that an estimator approaches its target in probability as sample size grows | M04-07 |
| selection bias | selection bias | Distinguish from sampling bias in general | Systematic optimism from selecting and reporting candidates using the same noisy evaluations | M04-07 |
| regression | regression | Distinguish from classification | Predicting a numerical target or its conditional distribution | M04-08 |
| classification | classification | Distinguish from regression | Predicting a finite class label or conditional class probabilities | M04-08 |
| population risk | population risk | Distinguish from training loss | Loss averaged over the target population | M04-08 |
| empirical risk | empirical risk | Distinguish from population risk | Loss averaged over an observed sample | M04-08 |
| empirical risk minimization | empirical risk minimization, ERM | Distinguish from directly minimizing population risk | The learning principle of minimizing average loss on an observed sample | M04-08 |
| squared loss | squared loss | Distinguish from absolute loss | The squared difference between a target and prediction | M04-08 |
| 0-1 loss | zero-one loss | Distinguish from a probability score | Loss equal to 1 for an incorrect class prediction and 0 for a correct prediction | M04-08 |
| Bayes classifier | Bayes classifier | Distinguish from Bayes' rule itself | The optimal classifier under 0-1 loss, choosing the class with the largest conditional probability | M04-08 |
| linear regression | linear regression | Do not equate with a causal-effect model | A regression model predicting a numerical target through an affine combination of features | M04-08 |
| logistic regression | logistic regression | Distinguish from linear regression | A classification model specifying binary log-odds through an affine combination of features | M04-08 |
| softmax regression | softmax regression | Distinguish from binary logistic regression | A model specifying categorical probabilities through softmax over class logits | M04-08 |
| regression residual | regression residual | Distinguish from a Taylor remainder | The observed target minus the regression prediction | M04-08 |
| mean absolute error | mean absolute error, MAE | Distinguish from MSE | The mean absolute difference between targets and predictions | M04-08 |
| confusion matrix | confusion matrix | Distinguish from a probability table | A table counting combinations of actual and predicted classes | M04-08 |
| accuracy | accuracy | Distinguish from calibration | The proportion of all predictions that are correct | M04-08 |
| precision | precision | Distinguish from recall | The proportion of positive predictions that are actual positives | M04-08 |
| recall | recall | Distinguish from precision | The proportion of actual positives identified as positive | M04-08 |
| class imbalance | class imbalance | Distinguish from model bias | Substantial differences in observed frequencies or base rates between classes | M04-08 |
| confidence interval | confidence interval | Distinguish from a Bayesian credible interval | An interval procedure containing the parameter at a specified rate under repeated sampling | M04-09 |
| confidence level | confidence level | Distinguish from posterior probability within an observed interval | A confidence interval procedure's target coverage $1-\alpha$ | M04-09 |
| coverage | coverage | Distinguish from inclusion in one interval | The proportion of intervals containing the target under repeated sampling | M04-09 |
| margin of error | margin of error | Distinguish from standard error | An interval's half-width obtained by multiplying a critical value by the standard error | M04-09 |
| z interval | z interval | Distinguish from a t interval | A confidence interval using a standard normal critical value | M04-09 |
| t interval | t interval | Distinguish from a z interval | An interval for a mean using an estimated standard deviation and a t critical value | M04-09 |
| t distribution | Student's t distribution | Distinguish from a Gaussian distribution | A distribution with heavier tails reflecting uncertainty in estimated population variance | M04-09 |
| bootstrap | bootstrap | Distinguish from sampling anew from the population | Approximating statistic variation by sampling with replacement from the observed empirical distribution | M04-09 |
| bootstrap replicate | bootstrap replicate | Distinguish from the original estimate | A statistic computed from one bootstrap resample | M04-09 |
| bootstrap standard error | bootstrap standard error | Distinguish from the standard deviation of raw data | The standard deviation of bootstrap replicates | M04-09 |
| percentile interval | percentile interval | Distinguish from a normal-form interval | An interval using two bootstrap-replicate quantiles as endpoints | M04-09 |
| paired bootstrap | paired bootstrap | Distinguish from independently resampling two groups | A bootstrap resampling paired observation units together | M04-09 |
| cluster bootstrap | cluster bootstrap | Distinguish from a rowwise iid bootstrap | A bootstrap resampling independent clusters as units | M04-09 |
| Monte Carlo error | Monte Carlo error | Distinguish from sampling bias | Numerical variation due to a finite number of simulation or resampling repetitions | M04-09 |
| null hypothesis | null hypothesis | Distinguish from a hypothesis established as true | A reference hypothesis determining the test statistic's reference distribution | M04-10 |
| alternative hypothesis | alternative hypothesis | Distinguish from the null hypothesis's posterior probability | A hypothesis expressing the difference or effect to be detected | M04-10 |
| test statistic | test statistic | Distinguish from the effect estimate itself | A statistic mapping a sample to a measure of extremeness under the null hypothesis | M04-10 |
| p-value | p-value | Distinguish from the probability that the null hypothesis is true | Under the null hypothesis, the probability of a statistic at least as extreme as the observed one | M04-10 |
| significance level | significance level | Distinguish from effect size | A rejection threshold chosen before analysis to control Type I error | M04-10 |
| Type I error | Type I error | Distinguish from Type II error | Rejecting a true null hypothesis | M04-10 |
| Type II error | Type II error | Distinguish from Type I error | Failing to reject the null hypothesis when a specified alternative is true | M04-10 |
| statistical power | statistical power | Distinguish from confidence level | The probability of rejecting the null hypothesis when a specified effect exists | M04-10 |
| effect size | effect size | Distinguish from a p-value | A quantity measuring the magnitude of the difference or relationship under study | M04-10 |
| multiple comparisons | multiple comparisons | Distinguish from a single test | Exploring or testing multiple hypotheses together | M04-10 |
| FWER | family-wise error rate | Distinguish from FDR | The probability of at least one false positive within a hypothesis family | M04-10 |
| Bonferroni correction | Bonferroni correction | Distinguish from an unadjusted per-test threshold | Controlling FWER by dividing the overall significance level by the number of hypotheses | M04-10 |
| FDR | false discovery rate | Distinguish from FWER | The expected proportion of false discoveries among rejected hypotheses | M04-10 |
| BH procedure | Benjamini-Hochberg procedure | Distinguish from Bonferroni correction | A procedure controlling FDR using sorted p-values and rank-dependent thresholds | M04-10 |
| log-likelihood | log-likelihood | Distinguish from likelihood | The natural logarithm of the likelihood, summing observation-level log terms for iid data | M04-11 |
| maximum likelihood estimation | maximum likelihood estimation, MLE | Distinguish from posterior maximization | Estimating parameters by maximizing the likelihood of observed data | M04-11 |
| maximum likelihood estimator | maximum likelihood estimator | Distinguish from an observed MLE value | A function of the sample that maximizes likelihood | M04-11 |
| negative log-likelihood | negative log-likelihood, NLL | Distinguish from probability itself | The negative of log-likelihood, used as a loss to minimize | M04-11 |
| MAP estimation | maximum a posteriori estimation | Distinguish from MLE | Estimation maximizing the posterior, combining likelihood and prior | M04-11 |
| model misspecification | model misspecification | Distinguish from optimization error | The situation where the true data distribution lies outside the chosen model family | M04-11 |
| self-information | self-information | Distinguish from the entropy average | The negative log-probability of one outcome | M04-12 |
| surprisal | surprisal | Distinguish from probability itself | The value $-\log p(x)$, which increases as probability decreases | M04-12 |
| nat | nat | Distinguish from a bit | The information unit based on natural logarithms | M04-12 |
| bit | bit | Distinguish from one binary outcome | The information unit based on base-2 logarithms | M04-12 |
| predictive entropy | predictive entropy | Distinguish from prediction error | Entropy summarizing the spread of model class probabilities for one input | M04-12 |
| soft target | soft target | Distinguish from a one-hot target | A target distribution placing probability mass on multiple classes | M04-12 |
| label smoothing | label smoothing | Distinguish from a guarantee of calibration | A training-target transformation distributing some one-hot mass to other classes | M04-12 |
| perplexity | perplexity | Do not directly compare values from different tokenizers and corpora | A language-model metric obtained by exponentiating average NLL per token | M04-12 |
| likelihood | likelihood | Distinguish its perspective from probability | A function evaluating hypotheses or parameters with observed evidence held fixed | M04-02 |
| entropy | entropy | Distinguish from a thermodynamic explanation | A distribution's average uncertainty | M04-12 |
| cross entropy | cross entropy | Distinguish from KL divergence | A model's negative log-probability averaged over the target distribution | M00-10 |
| KL divergence | Kullback–Leibler divergence | Not a symmetric distance | A directional difference from one distribution to another | M04-13 |
| log density ratio | log density ratio | Distinguish from a probability ratio | The logarithm of the ratio between two distributions' masses or densities at the same outcome | M04-13 |
| absolute continuity | absolute continuity | Distinguish from merely overlapping supports | A relation in which sets assigned zero probability by the reference distribution also receive zero probability from the compared distribution | M04-13 |
| forward KL | forward KL | Distinguish from reverse KL | The direction $D_{\mathrm{KL}}(p\Vert q)$, averaging over the target distribution | M04-13 |
| reverse KL | reverse KL | Distinguish from forward KL | The direction $D_{\mathrm{KL}}(q\Vert p)$, averaging over the approximation distribution | M04-13 |
| Gibbs' inequality | Gibbs' inequality | Distinguish from Jensen's inequality itself | The inequality stating that KL divergence is nonnegative | M04-13 |
| mutual information | mutual information | Not a causal effect | The extent to which one variable reduces uncertainty about another | M04-14 |
| joint entropy | joint entropy | Distinguish from a simple sum of marginal entropies | The average uncertainty of a pair of random variables' joint distribution | M04-14 |
| conditional entropy | conditional entropy | Distinguish from entropy at one particular condition | The average uncertainty remaining in one variable after observing another | M04-14 |
| pointwise mutual information | pointwise mutual information, PMI | Distinguish from overall mutual information | The log ratio of joint probability to the product of marginals for one outcome pair | M04-14 |
| marginal product | marginal product | Distinguish from the actual joint distribution | The independence model formed by multiplying two marginal distributions | M04-14 |
| Markov chain | Markov chain | Distinguish from an arbitrary list of variables | A variable relation in which the endpoints are conditionally independent given the middle variable | M04-14 |
| data processing inequality | data processing inequality | Distinguish from an estimator's finite-sample result | The inequality stating that postprocessing cannot increase mutual information about the source | M04-14 |
| calibration | calibration | Distinguish contextually from training adjustments | Agreement between predicted probabilities and actual frequencies | M04-15 |
| reliability diagram | reliability diagram | Distinguish from an accuracy plot | A plot comparing mean confidence and accuracy within confidence bins | M04-15 |
| ECE | expected calibration error | Does not prove full calibration | A summary weighting each bin's accuracy-confidence gap by its sample proportion | M04-15 |
| overconfidence | overconfidence | Distinguish from one incorrect answer | Predicted confidence exceeding the corresponding observed accuracy | M04-15 |
| underconfidence | underconfidence | Distinguish from low accuracy | Predicted confidence falling below the corresponding observed accuracy | M04-15 |
| scoring rule | scoring rule | Distinguish from accuracy alone | A rule assigning loss to a probability prediction and an observed outcome | M04-15 |
| proper scoring rule | proper scoring rule | Distinguish from an arbitrary probability loss | A rule whose expected score is minimized by reporting the true distribution | M04-15 |
| strictly proper scoring rule | strictly proper scoring rule | Distinguish from ties permitted by a proper scoring rule | A rule whose expected score is minimized only at the true distribution | M04-15 |
| Brier score | Brier score | Distinguish contextually from squared-loss regression | A score summing squared differences between probabilities and a one-hot outcome | M04-15 |
| log score | logarithmic score | Distinguish from a logit | The negative logarithm of the probability assigned to the observed outcome | M04-15 |
| sharpness | sharpness | Distinguish from calibration | The degree to which forecast probabilities concentrate away from the base rate | M04-15 |
| temperature scaling | temperature scaling | Distinguish from retraining a model | Calibration that changes probability concentration by adjusting logit magnitude with a positive temperature | M04-15 |
| causal effect | causal effect | Distinguish from association | The change in outcome when interventions differ | M04-16 |
| intervention | intervention | Distinguish from conditional observation | An operation externally setting a variable and changing the generating mechanism | M04-16 |
| do-operator | do-operator | Distinguish from conditioning | Notation for interventions, such as $\operatorname{do}(X=x)$ | M04-16 |
| causal graph | causal graph | Distinguish from an observational correlation graph | A graph expressing causal assumptions between variables through directed edges | M04-16 |
| DAG | directed acyclic graph | Distinguish from a graph with cycles | A directed graph with no directed cycles | M04-16 |
| confounder | confounder | Distinguish from a mediator or collider | A common cause of treatment and outcome | M04-16 |
| mediator | mediator | Distinguish from a confounder | An intermediate variable on a path from treatment effect to outcome | M04-16 |
| collider | collider | Distinguish from a confounder | A common effect where two causal arrows meet | M04-16 |
| potential outcome | potential outcome | Distinguish from one observed outcome | The outcome a unit would have under a specified treatment state | M04-16 |
| average treatment effect | average treatment effect, ATE | Distinguish from an individual effect | The population-average causal effect defined as $\mathbb E[Y(1)-Y(0)]$ | M04-16 |
| exchangeability | exchangeability | Distinguish from simple group equality | A condition making treatment groups comparable in terms of potential outcomes | M04-16 |
| positivity | positivity | Distinguish from requiring positive outcome probabilities | The condition that each compared treatment has positive probability within every confounder stratum | M04-16 |
| consistency | consistency | Distinguish from statistical consistency | The condition that the potential outcome corresponding to the received treatment equals the observed outcome | M04-16 |
| random assignment | random assignment | Distinguish from random sampling | Probabilistically assigning treatment independently of potential outcomes | M04-16 |
| experimental unit | experimental unit | Distinguish from an observation row | The smallest unit receiving independent treatment assignment or independent replicate generation | M04-17 |
| control condition | control condition | Distinguish from a treatment condition | A reference condition for comparing intervention effects | M04-17 |
| negative control | negative control | Distinguish from the target-effect condition | A control where the target effect should be absent, testing alternative explanations | M04-17 |
| positive control | positive control | Distinguish from the primary treatment | A control checking whether the pipeline detects a known effect | M04-17 |
| specificity control | specificity control | Distinguish from the target outcome alone | A control checking whether an intervention also harms unrelated behavior | M04-17 |
| sham intervention | sham intervention | Distinguish from modifying the target component | A control intervention using the same procedure without changing the target component | M04-17 |
| blocking | blocking | Distinguish from simple randomization over the entire sample | A design randomizing treatment within blocks similar in important characteristics | M04-17 |
| blinding | blinding | Distinguish contextually from data masking | Keeping evaluators or participants unaware of the condition | M04-17 |
| holdout set | holdout set | Distinguish from a validation set | Data reserved for final evaluation and not used for method selection | M04-17 |
| data leakage | data leakage | Distinguish from ordinary data sharing | Evaluation-outcome information entering fitting or selection | M04-17 |
| seed | random seed | Distinguish from an independent replicate | A value setting the initial state of a pseudorandom sequence | M04-17 |
| pseudoreplication | pseudoreplication | Distinguish from independent repetition | The error of counting dependent observations as independent replicates | M04-17 |
| preregistration | preregistration | Distinguish from prohibiting exploration | Recording hypotheses and an analysis plan before inspecting results | M04-17 |
| repeatability | repeatability | Distinguish from independent replication | The ability of the same team to rerun a computation with the same artifacts and environment | M04-17 |
| computational reproducibility | computational reproducibility | Distinguish from replication with new data | The ability of others to reproduce results using provided code, data, and environment | M04-17 |
| replication | replication | Distinguish from repeating the same execution | Retesting a scientific claim with an independent implementation, new data, or a new model | M04-17 |

## Neural networks

| Preferred term | English | Avoid or distinguish | Brief meaning | First lesson |
|---|---|---|---|---|
| axis | axis | Distinguish from a vector component or matrix rank | An independent direction for specifying tensor positions | N05-01 |
| dtype | data type | Distinguish from shape | The numerical representation format of tensor elements | N05-01 |
| device | device | Distinguish from a mathematical space | The CPU or accelerator location where a tensor is stored and operated on | N05-01 |
| broadcasting | broadcasting | Distinguish from directly copying values | A rule treating tensors as having the same shape when their trailing axes are compatible | N05-09 |
| autograd | automatic differentiation | Distinguish from symbolic algebra | A system composing derivative rules through executed tensor operations to compute gradient products | N05-10 |
| pre-activation | pre-activation | Distinguish from an activation | The affine output before applying an activation function | N05-02 |
| activation | activation | Distinguish from an activation function | An intermediate result after applying an activation function | N05-02 |
| activation function | activation function | Distinguish from an activation | A nonlinear function applied after a linear combination | N05-04 |
| gate | gate | Distinguish from an event probability | A computation using values on one path to modulate the elementwise magnitude and sign on another path | N05-04 |
| GLU | gated linear unit, GLU | Distinguish from a single ordinary activation | A structure multiplying a content projection and a sigmoid gate elementwise | N05-04 |
| SwiGLU | SwiGLU | Distinguish from a sigmoid GLU | A GLU variant applying SiLU to one projection before multiplying it elementwise with another | N05-04 |
| MLP | multilayer perceptron, MLP | Distinguish from an entire Transformer | A feed-forward network connecting affine layers and elementwise nonlinearities | N05-03 |
| logit | logit | Distinguish from a probability | A class score before softmax | M00-10 |
| softmax | softmax | Distinguish from argmax | A function converting logits to positive class probabilities summing to 1 | M00-10 |
| loss function | loss function | Distinguish from an evaluation metric | A scalar function minimized during learning | M00-10 |
| knowledge distillation | knowledge distillation | Distinguish from learning only from ground-truth labels | Training a student model using a teacher model's outputs or intermediate representations | M00-10 |
| black-box distillation | black-box distillation | Distinguish from distillation requiring access to teacher internals | Distillation training a student using only teacher output information | M00-10 |
| white-box distillation | white-box distillation | Distinguish from output-only distillation | Distillation accessing the teacher's intermediate representations or attention | M00-10 |
| backpropagation | backpropagation | Distinguish from an optimizer update | Computing gradients by propagating cotangents backward from a scalar loss | M03-14 |
| learning rate | learning rate | Distinguish from a derivative value | A positive quantity controlling the magnitude of a parameter update | M01-04 |
| mini-batch | mini-batch | Distinguish from the entire dataset | A group of samples selected for computing one training step's loss and gradient | N05-07 |
| momentum | momentum | Distinguish from the parameter itself | A method accumulating previous gradient directions in a buffer for updates | N05-08 |
| optimizer state | optimizer state | Distinguish from model parameters | Values stored for update computation, such as momentum buffers, moment estimates, and steps | N05-08 |
| AdamW | AdamW | Distinguish from an L2 penalty in Adam | An optimizer separating Adam's adaptive update from weight decay | N05-08 |
| weight decay | weight decay | Not always equivalent to adding an L2 penalty to the loss | Regularization applying a term proportional to parameter magnitude in the update | N05-08 |
| token | token | Not always a word or character | A string fragment used by a tokenizer vocabulary as an input-output unit | N05-11 |
| tokenizer | tokenizer | Distinguish from model weights | The rules and artifacts converting between text and token-ID sequences | N05-11 |
| embedding | embedding | Distinguish contextually from the entire embedding space | A representation mapping a discrete object to a continuous vector | N05-12 |
| unembedding | unembedding | Distinguish from the inverse of an embedding | A linear map sending hidden states to vocabulary logits | N05-12 |
| weight tying | weight tying | Distinguish from separate parameters with the same shape | A choice to share parameters between input embedding and output unembedding | N05-12 |
| RoPE | rotary position embedding, RoPE | Distinguish from adding absolute position information | A positional method rotating query-key feature pairs by position-dependent angles | N05-13 |
| query | query | Distinguish from the current token itself | An attention projection evaluating which keys to connect to | N05-14 |
| key | key | Distinguish from a past token itself | A projection forming dot products with queries to produce attention scores | N05-14 |
| value | value | Distinguish from an attention score | The content projection combined by attention-weighted summation | N05-14 |
| attention score | attention score | Distinguish from an attention probability | A scaled query-key dot product before softmax | N05-15 |
| causal mask | causal mask | Distinguish from a padding mask | A mask excluding future key positions from attention | N05-15 |
| MHA | multi-head attention, MHA | Distinguish from all heads sharing K and V | Attention using a separate key-value head for each query head | N05-16 |
| MQA | multi-query attention, MQA | Does not mean there is only one query head | Attention sharing one key-value head across all query heads | N05-16 |
| GQA | grouped-query attention, GQA | Not merely an alias for MHA or MQA | Attention sharing one key-value head within each query-head group | N05-16 |
| residual stream | residual stream | Distinguish from one residual connection | The representation path accumulated across Transformer layers | N05-17 |
| residual update | residual update | Distinguish from the entire stream after addition | A vector added to the residual stream by attention or an MLP | N05-17 |
| LayerNorm | layer normalization, LayerNorm | Distinguish from RMSNorm | Normalization subtracting the feature mean, scaling by variance, and applying a learned affine map | N05-18 |
| RMSNorm | root mean square layer normalization, RMSNorm | Does not perform mean centering | Normalization scaling by the root mean square of features | N05-18 |
| pre-norm | pre-norm | Distinguish from post-norm | An order feeding normalized output to a sublayer and then adding its update to the original residual | N05-18 |
| post-norm | post-norm | Distinguish from pre-norm | An order applying normalization after adding residual and sublayer output | N05-18 |
| dense MLP | dense MLP | Distinguish from a sparse expert layer | An MLP applying the same feed-forward parameters to every token | N05-19 |
| MoE | mixture of experts, MoE | Distinguish from ensembles in general | A structure whose router selects some expert subnetworks for each input | N05-19 |
| router | router | Distinguish from a SwiGLU feature gate | A computation assigning tokens to experts for execution | N05-19 |
| expert | expert | Not always an entire independent model | A feed-forward subnetwork selectively executed in an MoE | N05-19 |
| architecture diff | architecture diff | Distinguish from a performance ranking | An itemized comparison of model components, order, shapes, sharing, and implementation choices | N05-20 |
| teacher forcing | teacher forcing | Distinguish from allowing attention to the future | Using the ground-truth prefix as model input during training | N05-21 |
| label shift | label shift | Distinguish from dataset label noise | Alignment of a position's logits with the next token's label | N05-21 |
| KV cache | key-value cache | Distinguish from a full activation dump or learned memory | Past keys and values stored per layer for reuse during autoregressive inference | N05-22 |
| prefill | prefill | Distinguish from tokenwise decoding | The inference stage processing the whole prompt to produce the initial KV cache and final logits | N05-22 |
| decode step | decode step | Distinguish from one decoder block | An inference stage inputting a new token, updating the cache, and obtaining the next logits | N05-22 |
| greedy decoding | greedy decoding | Distinguish from sampling | A generation rule choosing the highest-logit token at each step | N05-23 |
| temperature | temperature | Distinguish from model weights or amount of knowledge | A positive quantity adjusting logit scale and probability concentration before sampling | N05-23 |
| top-k | top-k sampling | Distinguish from top-p | Sampling truncation retaining a fixed number of highest-logit candidates | N05-23 |
| top-p | nucleus sampling, top-p | Distinguish from a fixed candidate count | Truncation retaining the smallest leading candidate set based on cumulative probability mass | N05-23 |
| CoT faithfulness | chain-of-thought faithfulness | Distinguish from fluency or accuracy | The extent to which generated reasoning reflects the model process producing the answer | N05-24 |
| forward hook | forward hook | Distinguish from a forward pre-hook or backward hook | A callback invoked after a module computes its output | N05-25 |
| activation provenance | activation provenance | Distinguish from storing tensor values alone | A record connecting model, input, module, layer, token, dtype, and execution conditions | N05-25 |
| activation gradient | activation gradient | Distinguish from the activation value itself | Local sensitivity obtained by differentiating a scalar target with respect to an intermediate activation | N05-26 |
| first-order intervention estimate | first-order intervention estimate | Distinguish from an actual intervention effect | A target-change approximation using the inner product of an activation gradient and a perturbation | N05-26 |
| persistent buffer | persistent buffer | Distinguish from a learned parameter or optimizer state | A nonparameter tensor saved in a module's `state_dict` | N05-27 |
| strict load | strict load | Distinguish from silently ignoring some keys | Validation requiring an exact match between expected and loaded state keys | N05-27 |
| attention | attention | Do not treat as an explanation in itself | An operation forming a weighted sum of values from query-key scores | N05-15 |
| checkpoint | checkpoint | Distinguish from the final model | An artifact bundling model state, training state, and provenance at a specific training point | N05-27 |
| chain-of-thought | chain-of-thought, CoT | Do not equate with actual internal reasoning | A model-generated token sequence in the form of an intermediate explanation | N05-24 |

## Model interpretability

| Preferred term | English | Avoid or distinguish | Brief meaning | First lesson |
|---|---|---|---|---|
| model interpretability | model interpretability | Distinguish contextually from explainability | Research on understanding and testing model behavior and internal computation | I06-01 |
| representation | representation | Not always a single activation | How a model expresses input information in its internal state | I06-01 |
| behavioral metric | behavioral metric | Distinguish from an internal activation | A measurement defined on a model's input-output relation | I06-01 |
| representation question | representation question | Distinguish from a behavioral question | A question about an internal quantity with model, layer, token, and component fixed | I06-01 |
| activation dataset | activation dataset | Distinguish from a file containing only activation arrays | Data pairing selected activations with input, position, and execution provenance row by row | I06-02 |
| data leakage | data leakage | Distinguish from ordinary generalization | Evaluation information entering training, selection, or preprocessing | I06-02 |
| outlier | outlier | Does not automatically imply an error | An observation far from other samples according to a specified criterion | I06-03 |
| robust statistic | robust statistic | Distinguish from always removing outliers | A statistic relatively insensitive to extreme values | I06-03 |
| neuron-level analysis | neuron-level analysis | Do not assume a one-to-one relation with features | Analyzing one activation coordinate with model, module, layer, and token fixed | I06-04 |
| linear probe | linear probe | Distinguish from the model's actual readout | An auxiliary model measuring linear recoverability of labels from fixed activations | I06-06 |
| selectivity | selectivity | Distinguish from task accuracy alone | The difference between task-probe and matched-control performance | I06-07 |
| CKA | centered kernel alignment | Not invariant under all linear transformations | The degree of alignment between centered representation geometries | I06-08 |
| RSA | representational similarity analysis | Distinguish from comparing raw coordinates | An analysis comparing structures of similarities or distances between input pairs | I06-08 |
| feature visualization | feature visualization | Distinguish from causal attribution | Finding inputs and conditions strongly activating a feature to formulate response hypotheses | I06-09 |
| sparse coding | sparse coding | Distinguish from sparse activations themselves | Approximating a dense vector with a combination of few dictionary coefficients | I06-11 |
| dead feature | dead feature | Do not automatically equate with a rare feature | A latent never activated within a specified evaluation interval | I06-12 |
| feature stability | feature stability | Distinguish from proof of identifiability | The extent to which similar features reappear across independent training runs | I06-13 |
| probe | probe | Not evidence that the model actually uses the information | An auxiliary model recovering information from activations | I06-06 |
| superposition | superposition | Distinguish from a simple sum of features | More features represented through overlap within a limited number of dimensions | I06-10 |
| sparse autoencoder | sparse autoencoder, SAE | Does not guarantee unique features | A model reconstructing activations through sparse latents | I06-12 |
| attribution | attribution | Not equivalent to a causal explanation | An analysis allocating contributions of inputs or components to an output | I07-01 |
| sensitivity | sensitivity | Distinguish from an allocated explanatory share or causal effect | The local rate of output change for small input changes at a point | I07-01 |
| saliency | saliency | Distinguish from a signed gradient | Local sensitivity magnitude expressed, for example, by absolute input gradients | I07-02 |
| integrated gradients | integrated gradients, IG | Not baseline-independent attribution | Attribution integrating gradients along a path from baseline to input | I07-03 |
| perturbation attribution | perturbation attribution | Not a feature value independent of replacement values | Attribution using output differences before and after changing part of an input | I07-04 |
| internal intervention | internal intervention | Distinguish from observing activations | An experiment forcibly changing an intermediate node or edge message | I07-05 |
| ablation | ablation | Distinguish from patching | An intervention removing or disabling a component | I07-06 |
| activation patching | activation patching | Distinguish from observation alone | An intervention injecting activations from one execution into another | I07-07 |
| causal tracing | causal tracing | Distinguish from locating a single address for knowledge | Mapping the effects of restoring clean states by layer and token after corruption | I07-08 |
| path patching | path patching | Distinguish from patching an entire node | An intervention changing only edge or path messages from a sender to a specified receiver | I07-09 |
| direct logit attribution | direct logit attribution | Distinguish from an ablation effect | Direct logit contribution obtained by projecting a residual component onto an unembedding direction | I07-10 |
| circuit | circuit | Not a physical circuit | Internal computational components and paths producing a particular behavior | I07-11 |
| necessity | necessity | Distinguish from sufficiency | The property that removal impairs a function | I07-12 |
| sufficiency | sufficiency | Distinguish from necessity | The property that a structure alone restores a substantial part of a function | I07-12 |
| mediated effect | mediated effect | Distinguish from simple correlation or the total effect | The part of a treatment effect transmitted through a specified mediator path | I07-13 |
| off-manifold intervention | off-manifold intervention | Do not equate large effects with strong evidence | An intervention producing internal states outside the reference activation structure | I07-14 |
| sign-flip test | sign-flip test | Distinguish from an independent-samples t test | A test forming a null distribution by randomizing signs of paired differences | I07-15 |
| rationale dependence | rationale dependence | Not equivalent to overall CoT faithfulness | The extent to which answers change under rationale interventions | I07-16 |
| training dynamics | training dynamics | Distinguish from final-state analysis | Changes in parameters, representations, and behavior over training time | I08-01 |
| parameter distance | parameter distance | Distinguish from function distance | Distance between the weight coordinates of two models | I08-02 |
| function distance | function distance | Distinguish from parameter distance | Differences between two models' behavior under a specified input distribution and output metric | I08-02 |
| orthogonal Procrustes alignment | orthogonal Procrustes alignment | Distinguish from arbitrary invertible alignment | Alignment reducing correspondence error between representations through rotation or reflection | I08-03 |
| gradient flow | gradient flow | Not equivalent to a finite-step optimizer | Continuous-time dynamics whose velocity is the negative loss gradient | I08-04 |
| mode connectivity | mode connectivity | Distinguish from an actual training path | The connection of solutions by a parameter path maintaining low loss | I08-07 |
| influence function | influence function | Distinguish from exact leave-one-out retraining | A local approximation of how infinitesimal data-weight changes affect an optimum and prediction | I08-08 |
| feature emergence | feature emergence | Do not equate with a rise in one probe score | The appearance of evidence of feature formation, recovery, use, and behavior during training | I08-09 |
| grokking | grokking | Not equivalent to all delayed generalization | Delayed improvement in test generalization after fitting the training data | I08-10 |
| data attribution | data attribution | Distinguish from input-feature attribution | Estimating the learning influence of training examples related to a prediction | I08-12 |
| TracIn | TracIn | Distinguish from ground truth from removal retraining | Data attribution summing training-test gradient alignments across checkpoints | I08-12 |
| identifiability | identifiability | Distinguish from reproducibility | The property that observable functions or distributions uniquely determine parameters | M03-15 |

## Advanced theory

| Preferred term | English | Avoid or distinguish | Brief meaning | First lesson |
|---|---|---|---|---|
| manifold | manifold | Do not equate with a finite point cloud itself | A topological space that resembles Euclidean space near each point | A09-GEO-01 |
| coordinate chart | coordinate chart | Distinguish from the manifold itself | A map expressing an open region of a manifold in Euclidean coordinates | A09-GEO-01 |
| tangent space | tangent space | Distinguish from the entire ambient space | The vector space of possible curve velocities at a point | A09-GEO-02 |
| cotangent space | cotangent space | Do not equate with the tangent space | The space of linear functionals mapping tangent vectors to scalars | A09-GEO-02 |
| Riemannian metric | Riemannian metric | Does not mean only a distance function between points | A structure assigning smoothly varying inner products to tangent spaces | A09-GEO-03 |
| pullback metric | pullback metric | Not the unique metric of an input space | A metric transferring a map's output changes to lengths of input tangent vectors | A09-GEO-04 |
| connection | connection | Distinguish from simple coordinatewise subtraction | A rule comparing changes and transport of tangent vectors at different points | A09-GEO-05 |
| geodesic | geodesic | Not always a globally shortest path | A curve with zero covariant acceleration | A09-GEO-05 |
| intrinsic curvature | intrinsic curvature | Distinguish from visible bending of an embedding | Curvature determined by the manifold's internal metric alone | A09-GEO-06 |
| extrinsic curvature | extrinsic curvature | Distinguish from intrinsic curvature | How a manifold bends within an ambient space | A09-GEO-06 |
| local PCA | local principal component analysis | Distinguish from proof of a manifold | Approximating a tangent space by the leading subspace of neighborhood covariance | A09-GEO-07 |
| flow | flow | Distinguish from a single trajectory | A map sending every initial state to its state after a specified time | A09-DYN-01 |
| fixed point | fixed point | Do not automatically equate with a minimum | A state unchanged by the dynamics | A09-DYN-02 |
| basin of attraction | basin of attraction | Distinguish from local stability | The set of initial states converging to the same attractor | A09-DYN-03 |
| bifurcation | bifurcation | Distinguish from a mere abrupt change in a metric | A qualitative change in invariant structure or stability as a parameter changes | A09-DYN-03 |
| Markov property | Markov property | Distinguish from independence between states | The property that the future is independent of the past given the current state | A09-DYN-04 |
| stationary distribution | stationary distribution | Distinguish from rapid mixing | A state distribution unchanged by the transition | A09-DYN-04 |
| Langevin dynamics | Langevin dynamics | Do not automatically equate with SGD | Stochastic dynamics combining potential-gradient drift with Brownian diffusion | A09-DYN-05 |
| stochastic differential equation | stochastic differential equation, SDE | Distinguish from random-ODE notation | An equation specifying stochastic increments through drift and diffusion | A09-DYN-06 |
| Itô formula | Itô formula | Distinguish from the ordinary chain rule | A stochastic chain rule including a quadratic-variation correction | A09-DYN-06 |
| diffusion approximation | diffusion approximation | Distinguish from exact replication of a finite-step optimizer | An approximation representing small-step stochastic updates as an SDE | A09-DYN-07 |
| group | group | Distinguish from an arbitrary collection of transformations | A structure with a closed operation, associativity, an identity, and inverses | A09-SYM-01 |
| group action | group action | Distinguish from the group itself | A rule by which group elements consistently act as transformations of objects | A09-SYM-01 |
| stabilizer | stabilizer | Distinguish from an orbit | The subgroup of group elements fixing a specified object | A09-SYM-02 |
| gauge freedom | gauge freedom | Distinguish from a functional difference | Redundant coordinate freedom that leaves observables unchanged | A09-SYM-05 |
| linear representation | linear representation | Distinguish from a hidden representation | A map preserving group multiplication as composition of invertible linear maps | A09-SYM-06 |
| irreducible representation | irreducible representation | Not equivalent to a one-dimensional component | A linear representation with no nonzero proper invariant subspace | A09-SYM-06 |
| symmetry-aligned distance | symmetry-aligned distance | Distinguish from raw coordinate distance | Distance between objects minimized over permitted symmetry transformations | A09-SYM-07 |
| hypothesis class | hypothesis class | Distinguish from a learning algorithm | The set of predictors a learning algorithm can choose | A09-LRN-01 |
| generalization gap | generalization gap | Distinguish from distribution shift | The difference between population risk and training empirical risk | A09-LRN-03 |
| shattering | shattering | Distinguish from fitting one training set | The property that a class realizes every binary labeling of a finite point set | A09-LRN-04 |
| VC dimension | Vapnik–Chervonenkis dimension | Not equivalent to parameter count | The maximum number of points a class can shatter | A09-LRN-04 |
| Rademacher complexity | Rademacher complexity | Distinguish from random-label accuracy | A function class's expected ability to fit random signs on a sample | A09-LRN-05 |
| PAC learning | probably approximately correct learning | Distinguish from prediction confidence | A distribution-free learning guarantee expressed through permitted error and failure probability | A09-LRN-06 |
| sample complexity | sample complexity | Distinguish from runtime complexity | The sample count required for a specified accuracy-confidence guarantee | A09-LRN-06 |
| positive semidefinite kernel | positive semidefinite kernel | Distinguish from a linear map's kernel | A symmetric function whose every finite Gram matrix is positive semidefinite | A09-KER-02 |
| Gram matrix | Gram matrix | Do not automatically equate with a covariance matrix | A matrix of inner products or kernel values between sample pairs | A09-KER-02 |
| feature map | feature map | Distinguish from a unique meaning of coordinates | A map taking inputs to a feature space where the kernel inner product is defined | A09-KER-03 |
| kernel trick | kernel trick | Distinguish from an unconditional reduction in computation | Computing inner products through kernel values without explicit feature coordinates | A09-KER-03 |
| RKHS | reproducing kernel Hilbert space | Distinguish from an arbitrary function space | A Hilbert space expressing point evaluation as an inner product with a kernel section | A09-KER-04 |
| reproducing property | reproducing property | Distinguish from simply copying a function | The property reproducing evaluation through $f(x)=\langle f,k(x,\cdot)\rangle$ | A09-KER-04 |
| kernel integral operator | kernel integral operator | Distinguish from a finite Gram matrix | An operator acting on functions by integrating a kernel against a reference measure | A09-KER-05 |
| effective dimension | effective dimension | Distinguish from hard rank | A spectral dimension summing eigenvalue contributions at a regularization scale | A09-KER-05 |
| neural tangent kernel | neural tangent kernel, NTK | Distinguish from an activation-similarity kernel | A kernel defined by inner products of parameter gradients for different inputs | A09-KER-06 |
| kernel drift | kernel drift | Not equivalent to function distance | The change in empirical kernel geometry between checkpoints | A09-KER-08 |
| concentration of measure | concentration of measure | Distinguish from all points being identical | High-dimensional random quantities clustering around a mean or typical value | A09-RMT-01 |
| random projection | random projection | Distinguish from PCA | A map reducing representation dimension with a data-independent random matrix | A09-RMT-02 |
| aspect ratio | aspect ratio | Distinguish from sample count or dimension alone | The dimension-to-sample-count ratio $d/n$ in random matrix analysis | A09-RMT-03 |
| Marchenko–Pastur law | Marchenko–Pastur law | Not a universal formula for every covariance spectrum | The high-dimensional sample-covariance spectral distribution of iid isotropic noise | A09-RMT-04 |
| spectral bulk | spectral bulk | Distinguish from individual outliers | The continuous range containing most eigenvalues in a random-matrix limit | A09-RMT-04 |
| spiked covariance model | spiked covariance model | Distinguish from general anisotropic covariance | A model adding a low-rank signal to isotropic noise covariance | A09-RMT-05 |
| spectral separation | spectral separation | Distinguish from task relevance | Sample outlier eigenvalues separating from the noise bulk | A09-RMT-05 |
| parallel analysis | parallel analysis | Distinguish from a single analytic edge | A procedure comparing observed eigenvalues with simulated null-eigenvalue quantiles | A09-RMT-06 |
| subspace stability | subspace stability | Distinguish from matching eigenvector coordinates | The reproducibility of leading spans across splits or seeds | A09-RMT-06 |
| structural causal model | structural causal model, SCM | Distinguish from a correlation graph | A model defining a causal system through variables, structural equations, and an exogenous distribution | A09-CAU-01 |
| exogenous variable | exogenous variable | Distinguish from an endogenous variable | A variable whose values and distribution are supplied from outside the structural model | A09-CAU-01 |
| endogenous variable | endogenous variable | Not equivalent to observed variables in general | A variable whose structural equation determines its value from parents and exogenous variables | A09-CAU-01 |
| backdoor adjustment | backdoor adjustment | Distinguish from arbitrary covariate conditioning | A formula identifying an interventional distribution using a set blocking noncausal paths entering treatment | A09-CAU-03 |
| causal identifiability | causal identifiability | Distinguish from finite-sample estimation accuracy | The property that an observed distribution and assumptions uniquely determine a causal estimand | A09-CAU-03 |
| natural direct effect | natural direct effect, NDE | Distinguish from a treatment coefficient in regression | A treatment effect with the mediator held at its baseline counterfactual | A09-CAU-04 |
| natural indirect effect | natural indirect effect, NIE | Distinguish from simple mediator association | An effect changing the mediator's counterfactual world with treatment held fixed | A09-CAU-04 |
| causal abstraction | causal abstraction | Distinguish from probe decoding | An abstraction defining an implementation relation through corresponding low- and high-level intervention outcomes | A09-CAU-06 |
| transportability | transportability | Distinguish from reproducibility within the same dataset | The property that a causal effect identified in a source population can be transferred to a target population | A09-CAU-07 |
| effect heterogeneity | effect heterogeneity | Distinguish from sampling noise | Causal effects varying with context, subgroup, or model conditions | A09-CAU-07 |
