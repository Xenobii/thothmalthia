document.addEventListener("DOMContentLoaded", () => {

    function clampContinuous(input) {
        if (input.type !== "number") return;

        const min = parseFloat(input.min);
        const max = parseFloat(input.max);
        let val = parseFloat(input.value);

        if (isNaN(min) || isNaN(max)) return;

        if (!isNaN(val)) {
            if (val < min) input.value = min;
            if (val > max) input.value = max;
        }
    }

    function validate(param) {
        const lower = document.querySelector(`.advanced-lower[data-param="${param}"]`);
        const upper = document.querySelector(`.advanced-upper[data-param="${param}"]`);
        const error = document.querySelector(`.advanced-error[data-param="${param}"]`);

        if (!lower || !upper || !error) return;

        // Always clamp continuous ranges first
        clampContinuous(lower);
        clampContinuous(upper);

        const lowVal = parseFloat(lower.value);
        const upVal = parseFloat(upper.value);

        // Clear previous invalid state
        lower.classList.remove("is-invalid");
        upper.classList.remove("is-invalid");
        error.classList.add("d-none");
        error.classList.remove("d-block");

        const lowIsNumber = Number.isFinite(lowVal);
        const upIsNumber = Number.isFinite(upVal);

        // Only show error when both bounds are valid numbers and lower > upper
        if (lowIsNumber && upIsNumber && lowVal > upVal) {
            lower.classList.add("is-invalid");
            upper.classList.add("is-invalid");
            error.classList.remove("d-none");
            error.classList.add("d-block");
        }
    }

    const inputs = document.querySelectorAll(".advanced-lower, .advanced-upper");

    inputs.forEach(el => {
        el.addEventListener("input", () => validate(el.dataset.param));
        el.addEventListener("change", () => validate(el.dataset.param));
    });

    // initial validation for every parameter (ensures errors are hidden unless invalid)
    const params = new Set();
    inputs.forEach(el => params.add(el.dataset.param));
    params.forEach(p => validate(p));
});
